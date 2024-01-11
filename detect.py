import keras_ocr # type: ignore 
from dataclasses import dataclass 

pipeline = keras_ocr.pipeline.Pipeline(max_size=1024)

@dataclass 
class RelGroup: 
    words: set[str]
    max_misses: int

    def is_matched(self, all_words: set[str]) -> bool: 
        total_misses = sum(word not in all_words for word in self.words)
        return total_misses <= self.max_misses

relevant_words = {"copper, iron", "lead", "brass", "material", "type"}
relevant_groups = [RelGroup({"application", "new", "modified", "water", "service"}, 1), RelGroup({"second", "taxing", "district", "water", "department", "action", "taken"}, 1)]

def relevant_files(files: list[str]) -> list[str]:
    images = [
        keras_ocr.tools.read(file) for file in files
    ]

    # Each list of predictions in prediction_groups is a list of
    # (word, box) tuples.
    prediction_groups = pipeline.recognize(images)

    results: list[str] = []
    for file, group in zip(files, prediction_groups):
        all_words: list[str] = []
        for t in group:
            all_words.append(t[0].lower())
        all_words_set = set(all_words)
        if any(word in all_words_set for word in relevant_words) or any(rel_group.is_matched(all_words_set) for rel_group in relevant_groups):
            results.append(file)


    return results