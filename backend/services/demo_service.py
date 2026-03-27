from fastapi import Depends, HTTPException

from backend.repo.demo_repo import DemoRepository


class DemoService:
    def __init__(self, repo: DemoRepository = Depends(DemoRepository)):
        self.repo = repo

