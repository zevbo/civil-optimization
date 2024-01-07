


print("Importing Keras")
import keras_ocr # type: ignore 
print("Imported Keras")

pipeline = keras_ocr.pipeline.Pipeline()


relevant_words = {"copper, iron", "lead", "brass", "material"}

def is_maybe_relevant(file: str) -> bool:
    images = [
        keras_ocr.tools.read(file),
        keras_ocr.tools.read(file)
    ]

    # Each list of predictions in prediction_groups is a list of
    # (word, box) tuples.
    prediction_groups = pipeline.recognize(images)

    all_words: set[str] = set()
    for group in prediction_groups:
        for t in group:
            all_words.add(t[0].lower())

    return any(word in all_words for word in relevant_words)
    # img = Image.open(file)

    # text = pytesseract.image_to_string(img, lang="eng", config='--psm 6')

    # print(text)
print("Starting!")
r = is_maybe_relevant("00008039-1.png")
print(f"Might it be relevant? {r}")