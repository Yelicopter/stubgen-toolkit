from abc import ABC, abstractmethod
from typing import Iterable, List, Optional


class VectorStore(ABC):
    @abstractmethod
    def add_question_answer(
        self,
        queries: List[str],
        codes: List[str],
        ids: Iterable | None = None,
        metadatas: List | None = None,
    ) -> List:
        ...

    @abstractmethod
    def add_docs(
        self,
        docs: Iterable[str],
        ids: Iterable | None = None,
        metadatas: List | None = None,
    ) -> List:
        ...

    def update_question_answer(
        self,
        ids: Iterable,
        queries: List[str],
        codes: List[str],
        metadatas: List | None = None,
    ) -> List:
        ...

    def update_docs(
        self,
        ids: Iterable,
        docs: Iterable[str],
        metadatas: List | None = None,
    ) -> List:
        ...

    def delete_question_and_answers(self, ids: Iterable | None = None) -> bool | None:
        ...

    def delete_docs(self, ids: Iterable | None = None) -> bool | None:
        ...

    def delete_collection(self, collection_name: str) -> bool | None:
        ...

    def get_relevant_question_answers(self, question: str, k: int = 1) -> List:
        ...

    def get_relevant_docs(self, question: str, k: int = 1) -> List:
        ...

    def get_relevant_question_answers_by_id(self, ids: List) -> List:
        ...

    def get_relevant_docs_by_id(self, ids: List) -> List:
        ...

    @abstractmethod
    def get_relevant_qa_documents(self, question: str, k: int = 1) -> List:
        ...

    @abstractmethod
    def get_relevant_docs_documents(self, question: str, k: int = 1) -> List:
        ...

    def _format_qa(self, query: str, code: str) -> str:
        ...
