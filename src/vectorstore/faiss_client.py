import os
import pickle

import faiss
import numpy as np


class FAISSClient:

    def __init__(
        self,
        dimension=384,
        index_path="data/vectorstore/faiss.index",
        mapping_path="data/vectorstore/mapping.pkl"
    ):

        self.dimension = dimension

        self.index_path = index_path

        self.mapping_path = mapping_path

        self.chunk_mapping = {}

        self.current_index = 0

        os.makedirs(
            "data/vectorstore",
            exist_ok=True
        )

        self._load_or_create()

    def _load_or_create(self):

        if os.path.exists(
            self.index_path
        ):

            self.index = faiss.read_index(
                self.index_path
            )

            if os.path.exists(
                self.mapping_path
            ):

                with open(
                    self.mapping_path,
                    "rb"
                ) as file:

                    self.chunk_mapping = (
                        pickle.load(file)
                    )

                self.current_index = (
                    len(
                        self.chunk_mapping
                    )
                )

        else:

            self.index = (
                faiss.IndexFlatL2(
                    self.dimension
                )
            )

    def save(self):

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(
            self.mapping_path,
            "wb"
        ) as file:

            pickle.dump(
                self.chunk_mapping,
                file
            )

    def add_document(
    self,
    embedding,
    chunk_id
   ):

     vector = np.array(
        [embedding],
        dtype="float32"
    )

     self.index.add(
        vector
    )

     self.chunk_mapping[
        self.current_index
    ] = {

        "chunk_id": chunk_id

    }

     self.current_index += 1

     self.save()

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = (
            self.index.search(
                query_vector,
                top_k
            )
        )

        results = []

        for idx in indices[0]:

            if idx in self.chunk_mapping:

                results.append(
                    self.chunk_mapping[idx]
                )

        return results

    def get_total_vectors(self):

        return self.index.ntotal

    def reset(self):

        if os.path.exists(
            self.index_path
        ):
            os.remove(
                self.index_path
            )

        if os.path.exists(
            self.mapping_path
        ):
            os.remove(
                self.mapping_path
            )

        self.chunk_mapping = {}

        self.current_index = 0

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        print(
            "FAISS index reset successfully."
        )