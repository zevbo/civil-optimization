import keras_ocr # type: ignore 
from dataclasses import dataclass 

pipeline = keras_ocr.pipeline.Pipeline(max_size=1024)

@dataclass 
class RelGroup: 
    words: set[str]
    max_misses: int
    sub_group: str | None = None

    def is_matched(self, all_words: set[str]) -> bool: 
        total_misses = sum(word not in all_words for word in self.words)
        return total_misses <= self.max_misses

relevant_words = {"copper, iron", "lead", "brass", "material", "type"}
relevant_groups = [RelGroup({"application", "new", "modified", "water", "service"}, 1), RelGroup({"second", "taxing", "district", "water", "department", "action", "taken"}, 1, "second_taxing_district")]

@dataclass 
class RelevantFile:
    file: str 
    sub_group: str | None = None

def relevant_files(files: list[str]) -> list[RelevantFile]:
    images = [
        keras_ocr.tools.read(file) for file in files
    ]

    # Each list of predictions in prediction_groups is a list of
    # (word, box) tuples.
    prediction_groups = pipeline.recognize(images)

    results: list[RelevantFile] = []
    for file, group in zip(files, prediction_groups):
        all_words: list[str] = []
        for t in group:
            all_words.append(t[0].lower())
        all_words_set = set(all_words)
        if any(word in all_words_set for word in relevant_words):
            results.append(RelevantFile(file))
        else:
            for rel_group in relevant_groups:
                if rel_group.is_matched(all_words_set):
                    results.append(RelevantFile(file, sub_group=rel_group.sub_group))
                    break 


    return results