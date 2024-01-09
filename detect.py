# import keras_ocr # type: ignore 
import easyocr

# pipeline = keras_ocr.pipeline.Pipeline()

relevant_words = {"copper, iron", "lead", "brass", "material"}

reader = easyocr.Reader(['en'])
def relevant_files(files: list[str]) -> list[str]:
    all_results = [
        # keras_ocr.tools.read(file) 
        reader.readtext(file)
        for file in files
    ]

    results: list[str] = []
    for file, this_results in zip(files, all_results):
        all_words: set[str] = set()
        for t in this_results:
            all_words.add(t[1].lower())
        if any(word in all_words for word in relevant_words):
            results.append(file)

    return results