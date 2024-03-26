import bcrypt
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from utils.getUserByToken import get_current_user

from database import get_db

from schemas.Response.Response import Response
from schemas.common.SharedDocBase import SharedDocBase

from models.Doc import Doc
from models.User import User
from models.SharedDoc import SharedDoc

router = APIRouter(prefix="/me/share", tags=["Docs Share"])


@router.post("/", response_model=Response)
def shareDocs(docShareDTO: SharedDocBase, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user:
        return {"message": "Unauthorized", "success": False}

    # check if user is the owner of the document
    doc = db.query(Doc).filter(Doc.owner_id == user["id"], Doc.id == docShareDTO.doc_id).first()
    if not doc:
        return {"message": "Doc not found", "success": False}

    # check if user mail exists
    target_user = db.query(User).filter(User.email == docShareDTO.user_mail).first()

    if not target_user:
        return {"message": "Target user not found", "success": False}

    # check if user is trying to share the document with himself
    if doc.owner_id == target_user.id:
        return {"message": "You can't share the document with yourself", "success": False}

    # check if the document is already shared with the target_user

    shared_doc = db.query(SharedDoc).filter(SharedDoc.doc_id == docShareDTO.doc_id,
                                            SharedDoc.user_id == target_user.id).first()

    if shared_doc:
        return {"message": "Doc already shared with the target user", "success": False}

    # share the document
    doc_share = SharedDoc(doc_id=docShareDTO.doc_id, user_id=target_user.id, edit_access=docShareDTO.edit_access)
    db.add(doc_share)
    db.commit()
    db.refresh(doc_share)

    return {"message": "Doc shared", "success": True}


@router.patch("/", response_model=Response)
def updateShareAccess(docShareDTO: SharedDocBase, db: Session = Depends(get_db),
                      user=Depends(get_current_user)):
    if not user:
        return {"message": "Unauthorized", "success": False}

    # check if user is the owner of the document
    doc = db.query(Doc).filter(Doc.owner_id == user["id"], Doc.id == docShareDTO.doc_id).first()
    if not doc:
        return {"message": "Doc not found", "success": False}

    # check if user mail exists
    target_user = db.query(User).filter(User.email == docShareDTO.user_mail).first()

    if not target_user:
        return {"message": "Target user not found", "success": False}

    # check if user is trying to share the document with himself
    if doc.owner_id == target_user.id:
        return {"message": "You can't share the document with yourself", "success": False}

    # check if the document is already shared with the target_user

    shared_doc = db.query(SharedDoc).filter(SharedDoc.doc_id == docShareDTO.doc_id,
                                            SharedDoc.user_id == target_user.id).first()

    if not shared_doc:
        return {"message": "Doc not shared with the target user", "success": False}

    shared_doc.edit_access = docShareDTO.edit_access
    db.commit()
    db.refresh(shared_doc)

    return {"message": "Doc shared access updated", "success": True}


@router.delete("/", response_model=Response)
def deleteShare(docShareDTO: SharedDocBase, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user:
        return {"message": "Unauthorized", "success": False}

    # check if user is the owner of the document
    doc = db.query(Doc).filter(Doc.owner_id == user["id"], Doc.id == docShareDTO.doc_id).first()
    if not doc:
        return {"message": "Doc not found", "success": False}

    # check if user mail exists
    target_user = db.query(User).filter(User.email == docShareDTO.user_mail).first()

    if not target_user:
        return {"message": "Target user not found", "success": False}

    # check if user is trying to share the document with himself
    if doc.owner_id == target_user.id:
        return {"message": "You can't share the document with yourself", "success": False}

    # check if the document is already shared with the target_user

    shared_doc = db.query(SharedDoc).filter(SharedDoc.doc_id == docShareDTO.doc_id,
                                            SharedDoc.user_id == target_user.id).first()

    if not shared_doc:
        return {"message": "Doc not shared with the target user", "success": False}

    db.delete(shared_doc)
    db.commit()

    return {"message": "Doc shared access deleted", "success": True}
