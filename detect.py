import keras_ocr # type: ignore 

pipeline = keras_ocr.pipeline.Pipeline(max_size=4096)

relevant_words = {"copper, iron", "lead", "brass", "material"}

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
        print(f"{all_words = }")
        all_words_set = set(all_words)
        if any(word in all_words_set for word in relevant_words):
            results.append(file)

    return results