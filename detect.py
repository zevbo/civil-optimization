import keras_ocr # type: ignore 

pipeline = keras_ocr.pipeline.Pipeline()

relevant_words = {"copper, iron", "lead", "brass", "material"}

def relevant_files(files: list[str]) -> list[str]:
    images = [
        keras_ocr.tools.read(file) for file in sorted(files)
    ]

    # Each list of predictions in prediction_groups is a list of
    # (word, box) tuples.
    prediction_groups = pipeline.recognize(images)

    results: list[str] = []
    for file, group in zip(files, prediction_groups):
        all_words: set[str] = set()
        for t in group:
            all_words.add(t[0].lower())
        if any(word in all_words for word in relevant_words):
            results.append(file)

    return results