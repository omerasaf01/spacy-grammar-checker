import spacy
from dtos.responses.checking_response import CheckingResponseDto

nlp = spacy.load("xx_ent_wiki_sm") # Low accuracy
nlp.add_pipe('sentencizer')

COMMON_MISTAKES = {
    "gelcek": "gelecek",
    "gidicem": "gideceğim",
    "olucak": "olacak",
    "değilmi": "değil mi"
}

def check_subject_verb_agreement(text):
    doc = nlp(text)
    errors = []

    for sent in doc.sents:
        has_subject = False
        has_verb = False

        for token in sent:
            if token.dep_ == "nsubj" or token.pos_ in ["NOUN", "PRON"]:
                has_subject = True
            if token.pos_ == "VERB":
                has_verb = True

        if has_subject and not has_verb:
            errors.append(f"{sent.text.strip()} cümlesinde yüklem eksik olabilir")
        if has_verb and not has_subject:
            errors.append(f"{sent.text.strip()} cümlesinde özne eksik olabilir")

    return errors


def check_common_mispellings(text):
    doc = nlp(text)
    errors = []

    for token in doc:
        if token.text.lower() in COMMON_MISTAKES:
            suggestion = COMMON_MISTAKES[token.text.lower()]
            errors.append(f"'{token.text}' yerine '{suggestion}' olabilir")

    return errors

def check_grammar(text):
    suggestions = []
    suggestions += check_subject_verb_agreement(text)
    suggestions += check_common_mispellings(text)
    response = CheckingResponseDto(suggestions=suggestions)

    return response
