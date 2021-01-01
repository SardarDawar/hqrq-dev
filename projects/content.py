from .vars import *
from scripts.topic_expressor import q_what
import spacy
nlp = spacy.load("en_core_web_sm")

PROJ_TYPE_LIST = {
    PROJ_TYPE_ANALYSIS_REPORT: PROJ_TEXT_TYPE_ANALYSIS_REPORT,
    PROJ_TYPE_COMPLIANCE_DOCUMENT: PROJ_TEXT_TYPE_COMPLIANCE_DOCUMENT,
    PROJ_TYPE_CREATIVE_CONTENT: PROJ_TEXT_TYPE_CREATIVE_CONTENT, 
    PROJ_TYPE_RATIONALE: PROJ_TEXT_TYPE_RATIONALE,
    PROJ_TYPE_DIRECT_COMMUNICATION: PROJ_TEXT_TYPE_DIRECT_COMMUNICATION,
    PROJ_TYPE_PERSUASIVE_PIECE: PROJ_TEXT_TYPE_PERSUASIVE_PIECE, 
    PROJ_TYPE_PROMOTIONAL_CONTENT: PROJ_TEXT_TYPE_PROMOTIONAL_CONTENT, 
    PROJ_TYPE_BUSINESS_PROPOSAL: PROJ_TEXT_TYPE_BUSINESS_PROPOSAL,
    PROJ_TYPE_REQUIREMENTS_DOCUMENT: PROJ_TEXT_TYPE_REQUIREMENTS_DOCUMENT,
    PROJ_TYPE_FUTURE_SCENARIO: PROJ_TEXT_TYPE_FUTURE_SCENARIO, 
    PROJ_TYPE_TECHNICAL_DOCUMENT: PROJ_TEXT_TYPE_TECHNICAL_DOCUMENT,
    PROJ_TYPE_TRAINING_PROGRAM: PROJ_TEXT_TYPE_TRAINING_PROGRAM,
}

PROJ_SUBTYPE_CHOICES_SEL_LIST = {
    PROJ_TYPE_ANALYSIS_REPORT: {
        PROJ_SUBTYPE_ASSESSMENT: PROJ_TEXT_SUBTYPE_ASSESSMENT,
        PROJ_SUBTYPE_REVIEW: PROJ_TEXT_SUBTYPE_REVIEW,
        PROJ_SUBTYPE_REPORT: PROJ_TEXT_SUBTYPE_REPORT,
        PROJ_SUBTYPE_COMPARISON: PROJ_TEXT_SUBTYPE_COMPARISON,
    }, 
    PROJ_TYPE_COMPLIANCE_DOCUMENT: {
        PROJ_SUBTYPE_POLICY_DOCUMENT: PROJ_TEXT_SUBTYPE_POLICY_DOCUMENT,
        PROJ_SUBTYPE_PROCEDURES_DOCUMENT: PROJ_TEXT_SUBTYPE_PROCEDURES_DOCUMENT,
    },
    PROJ_TYPE_CREATIVE_CONTENT: {
        PROJ_SUBTYPE_CREATIVE_FICTION: PROJ_SUBTYPE_CREATIVE_FICTION,
        PROJ_SUBTYPE_CREATION_NON_FICTION: PROJ_SUBTYPE_CREATION_NON_FICTION,
    }, 
    PROJ_TYPE_RATIONALE: {
        PROJ_SUBTYPE_DECISION_RATIONALE: PROJ_TEXT_SUBTYPE_DECISION_RATIONALE,
        PROJ_SUBTYPE_SELECTION_ANALYSIS: PROJ_TEXT_SUBTYPE_SELECTION_ANALYSIS,
        PROJ_SUBTYPE_RECOMMENDATION: PROJ_TEXT_SUBTYPE_RECOMMENDATION,
    }, 
    PROJ_TYPE_DIRECT_COMMUNICATION: {
        PROJ_SUBTYPE_EMAIL: PROJ_TEXT_SUBTYPE_EMAIL,
        PROJ_SUBTYPE_LETTER: PROJ_TEXT_SUBTYPE_LETTER,
        PROJ_SUBTYPE_MEMO: PROJ_TEXT_SUBTYPE_MEMO,
        PROJ_SUBTYPE_NOTICE: PROJ_TEXT_SUBTYPE_NOTICE,
        PROJ_SUBTYPE_NEWSLETTER: PROJ_TEXT_SUBTYPE_NEWSLETTER,
    },
    PROJ_TYPE_PERSUASIVE_PIECE: {
        PROJ_SUBTYPE_ESSAY: PROJ_TEXT_SUBTYPE_ESSAY,
        PROJ_SUBTYPE_ARTICLE: PROJ_TEXT_SUBTYPE_ARTICLE,
        PROJ_SUBTYPE_BLOG_POST: PROJ_TEXT_SUBTYPE_BLOG_POST,
        PROJ_SUBTYPE_E_BOOK: PROJ_TEXT_SUBTYPE_E_BOOK,
        PROJ_SUBTYPE_BOOK: PROJ_TEXT_SUBTYPE_BOOK,
        PROJ_SUBTYPE_WHITEPAPER: PROJ_TEXT_SUBTYPE_WHITEPAPER,
    }, 
    PROJ_TYPE_PROMOTIONAL_CONTENT: {
        PROJ_SUBTYPE_WEBSITE: PROJ_TEXT_SUBTYPE_WEBSITE,
        PROJ_SUBTYPE_LANDING_PAGE: PROJ_TEXT_SUBTYPE_LANDING_PAGE,
        PROJ_SUBTYPE_ADVERTISEMENT: PROJ_TEXT_SUBTYPE_ADVERTISEMENT,
        PROJ_SUBTYPE_FLIER: PROJ_TEXT_SUBTYPE_FLIER,
        PROJ_SUBTYPE_BROCHURE: PROJ_TEXT_SUBTYPE_BROCHURE,
    }, 
    PROJ_TYPE_BUSINESS_PROPOSAL: {
        PROJ_SUBTYPE_PROPOSAL: PROJ_TEXT_SUBTYPE_PROPOSAL,
        PROJ_SUBTYPE_QUOTE: PROJ_TEXT_SUBTYPE_QUOTE,
        PROJ_SUBTYPE_POTENTIAL_SCENARIO: PROJ_TEXT_SUBTYPE_POTENTIAL_SCENARIO,
    },
    PROJ_TYPE_REQUIREMENTS_DOCUMENT: {
        PROJ_SUBTYPE_SCOPE: PROJ_TEXT_SUBTYPE_SCOPE,
        PROJ_SUBTYPE_CHARTER: PROJ_TEXT_SUBTYPE_CHARTER,
        PROJ_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT: PROJ_TEXT_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT,
    }, 
    PROJ_TYPE_FUTURE_SCENARIO: {
        PROJ_SUBTYPE_STRATEGY: PROJ_TEXT_SUBTYPE_STRATEGY,
        PROJ_SUBTYPE_PLAN: PROJ_TEXT_SUBTYPE_PLAN,
        PROJ_SUBTYPE_GOAL_OUTLINE: PROJ_TEXT_SUBTYPE_GOAL_OUTLINE,
        PROJ_SUBTYPE_DEFINITION_DOCUMENT: PROJ_TEXT_SUBTYPE_DEFINITION_DOCUMENT,
    }, 
    PROJ_TYPE_TECHNICAL_DOCUMENT: {
        PROJ_SUBTYPE_HOW_TO_ARTICLE: PROJ_TEXT_SUBTYPE_HOW_TO_ARTICLE,
        PROJ_SUBTYPE_PATENT_SPECIFICATION: PROJ_TEXT_SUBTYPE_PATENT_SPECIFICATION,
        PROJ_SUBTYPE_PRODUCT_MANUAL: PROJ_TEXT_SUBTYPE_PRODUCT_MANUAL,
    },
    PROJ_TYPE_TRAINING_PROGRAM: {
        PROJ_SUBTYPE_CURRICULUM: PROJ_TEXT_SUBTYPE_CURRICULUM,
        PROJ_SUBTYPE_TRAINING_DOCUMENT: PROJ_TEXT_SUBTYPE_TRAINING_DOCUMENT,
    },
}

PROJ_TOPIC_CHOICES_LIST = {
    PROJ_TOPIC_PERSON: PROJ_TEXT_TOPIC_PERSON,
    PROJ_TOPIC_COMPANY: PROJ_TEXT_TOPIC_COMPANY,
    PROJ_TOPIC_GROUP: PROJ_TEXT_TOPIC_GROUP,
    PROJ_TOPIC_PRODUCT_SERVICE: PROJ_TEXT_TOPIC_PRODUCT_SERVICE,
    PROJ_TOPIC_CONCEPT_THING: PROJ_TEXT_TOPIC_CONCEPT_THING,
    PROJ_TOPIC_PLACE_DEST_BUILDING: PROJ_TEXT_TOPIC_PLACE_DEST_BUILDING,
}

PROJ_TYPE_SVGS = {
    PROJ_TYPE_ANALYSIS_REPORT: f'<svg width="63" height="61" viewBox="0 0 63 61" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="63" height="61" fill="url(#pattern0)"/><defs><pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image0" transform="translate(0 -0.0035903) scale(0.00826446 0.00853543)"/></pattern><image id="image0" width="121" height="118" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHkAAAB2CAMAAADbcsyuAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAzUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKMFRskAAAAQdFJOUwAQIDBAUGBwgI+fr7/P3+8jGoKKAAAACXBIWXMAABcRAAAXEQHKJvM/AAAEM0lEQVRoQ+2a67ajIAyFa8VWq5a+/9OOrdlcUmhDsM6aNX5/zhILWyAJAc7p4ODg4P+haU13uXTGNFSwB43pZ/vwjENHb35KY26hKhgv9P5XmDElu/JLcTORSIb5R9rnId9fMJ7pxxvSCHSfDFtrt3dqOcDa1MdYQ1W2wcQadrya9vz05PPi1SOVgutaZxOuobAdWh49utjTeiquprlRi0+mlkoZXTgdExVW0gSj+clvroH2vElM9T22188NXul3C1v02jc3f3WYwANuVKSnc7YzCkaw8VGuNp61TlhosAP9/PGo8+tmpmbQBXoKYVPaU/HDVkUz18xABQ/66+m5tLPIkQo0nDHWzl4Syv3EpN1cZ1xfAj7fu2dK+cSkG1j4TAXlwLyCGUsqc+nzWu3xUGdJGLZgCUgrc2mYx52eSzGoHzhyRplJu/FWOjXidVg9p8ykL1TV0nMZDc1y1GRWmUmj0yqf7qhyFIvyyrE0KquyBBrs2DUSylNPRKNDnVY5FtVFl1belQ3pLoQvEQoUw50c7IRyQPiyYrjJJ9lwiZWbtbomeNMqhaWCECtjuBV+RdPMAqBcGblMcUaG2MvWG7ly2k4EIHQy25Qrt9RAsYkh/tEjkCvDxGKvFEDKfLWRKyNxKlYmA+ExqECZwn5x+kvK3B0LlMkttcoVfSa3ZAHhOzTPPBAUKK8NlM8z3JEegVwZAaE4LYEyC0FyZfhzcRYId1THMASE8k0OOQULQXJlxO3yBZqcgrmVXJlSZkXiS5tCZtxi5Yr1GUtGbJtiZQy2JuOmSBDHILEyknVN2ptMKqTKSNZVuSc8OhovqTJ2VsWx8wlsJOq0UBldVh5ZIGX+vK8K8C/RZeWxAeJf2GmZsjtr0G6gYZ/BciNTxmiF+98i3N7fz5ZIGb5cvkI68O3WrRtUkGH9jTtDU3fZm3dR9HWTrDTsFXceFm3LP+IPIFW+DPwZoNQ//Jl0xVg/cSFBeGQdnPbWXtxhyQrNLE943yGfoAzIaha+rnjRfUe9NFxr4fNFmHFGQVRL+9PyxV6z2m3whaBa2p+WLwzJ6TbpK7xqaRcOX9ghDhGNGbxFM+7zfew1eQnwFk6Mt/5iTNtd+2FivU3cGdbElJZbT5a58+HHUXV/FY94jteV1tbS0SVhBro79JHPUXdrl3KckKlD8369ctRJf9K20V1pSppeqelSnmsn7joJs6iWXnysn7wD20X17UI6bZAbSD9pTdd1JqG54nKKkI2kP4MdSswe0i6Fi9lDOuMFO0gnosmLHaTfVhmieuX8ziEd8hel6//z4is56Zotl5B0LHs7Q/4FmVxGsGGpJi2tuqQtJSmtPLspJCW9g3U/SUjvMtoL79K1u2sxXLryQKEEJq05fNYSJWb7WDYIDh+mmt2lAhwb2b3sOuB86cdUcn5wcHDwr3I6/QFpZpGk5dMJYwAAAABJRU5ErkJggg=="/></defs></svg>', 
    PROJ_TYPE_COMPLIANCE_DOCUMENT: f'<svg width="71" height="69" viewBox="0 0 71 69" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="71" height="69" fill="url(#pattern1)"/><defs><pattern id="pattern1" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image1" transform="translate(-0.00704225) scale(0.0084507 0.00869565)"/></pattern><image id="image1" width="120" height="115" xlink:href="data:image/png;base64,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"/></defs></svg>',
    PROJ_TYPE_CREATIVE_CONTENT: f'<svg width="63" height="61" viewBox="0 0 63 61" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="63" height="61" fill="url(#pattern2)"/><defs><pattern id="pattern2" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image2" transform="translate(-0.000966184) scale(0.0084196 0.00869565)"/></pattern><image id="image2" width="119" height="115" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHcAAABzCAYAAACiqJ2cAAAGOklEQVR4Ae2aC83sNhBGDaEQCuFCKIRCKIRCKIMLoRAKoRAKoRAuhFZH+i1Zoxk7Dzvx2p+lKLvZPOzzzcvOpqQmAiIgAiIgAiIgAiIgAiIgAiIgAiIgAiIgAiIgAiIgAiIgAiIgAqsR+J5S+pFSYq+2EIFvKaX/iu23hca2/VAQsxRX3ruQSUjchcS0Q5G4lshC3yXuQmLaoUhcS2Sh7xJ3ITHtUCSuJbLQ95/MVOjXhcamoaSUfk8p/ZNS+iOlhNhqgwn88gWbsLlaY1Vs24b3sNabV45WWTVCVCIE4/p3V3Xx2ixs3n+6wAiLoHk87EkHW7Zs4SWMEQITJX5OKQGf/YjmCcu4MOItG9B7C8w98Za/v+5dhv7SiDjOs/9KKd3N+ZGwIwz1owylh8B4I1WwZyiloK3PCH02jErYhrlFArdCKNfhHZF3tsSMfud+R73ZM6jtPdbq7QkcLTZwLp7aW1QrNsLVRF6xKLS6dPuOaIRGIJMz+W4bYdDzFitMz+/0JWpldSyPjSgVxz1R+RlPOeOtnIshYDCAx9vZIxbbGQPgPlGaIE9jdGoXCQDwiLCIgIhHYRP6EfzIvTln26nNRd2alyFsy8vwxLvgeU4ZZqNnHjWc5sB2P6EVihEDUaJQfoVfy5jw4ChEX3neltfgIbVwibeOgtx6NkaldpEAnlirismTPb3V62arDxiX2gUCFEVRzkPYp1pL4Ggu/lT/Pu45AI3CMd482mMtsFp/FJ4trcZ3PNPzWkA+LWzuKjnY6xPHaqtY+XrtvwqkyGvfhvhnIDD9VTtAIMq1MxQvRA2ih+fBbxveAbTvnxLBu7tA0WtkiOiJi1erVQhEeY0iapaG93riKjQ3FIpCMsdnalHu1bSoolJ+3Wc9Y9QqVKUr1Z+i0DybEVYH8fSPXr6dKSRnHlFoxjjVAgLWY/k+Q5Xsddebrs1oiF7fLx+jKGKQDD7avHVhQq8n7pNLjWcGzRhtf72iKvOw55bf8XjOm77haWXHo8926sBUxzt31jwW1Qd2Be0qjymF9vKmJ5rNT1Sa3nmzLg5EFbMV9yqPKcXFA1sDwprtokQkLi/OZ2yR59rKnnF6Ibw0ZHh8RFjOQmDB0ZbPKfecWw44f541LHvhFqNWcwhE4trw7Vz6yiEvOi1fLd8h7U0vvAr0zjN6XBsZIt6sFhCIcpPNY8Hljx2O6oNZp22Pgak9KHpJP1tRFRVTWluuqBstZMwU7gjJXr4lffCbWoWAB47KeZbQHP2nedbCr4L6+Z+ixYEZ4EVei/HNljqeV+7AE6PQDEC78HHgdl1PibyWaKOQfBB15L1v5jVWkLypGkY360LLQdzPnlbz3jeKK7wymqa9aXDPqtLxaZH3vpHfoqnPG33piPi9W9W8BahPLbRHeZY+YIBqFwnUwjNFzOhWy7MqojrQj5b68JyR06Na5CDPvl25d0A7xy1qOW/Ukh8VMAbkbZrTdraLqFodEZ5JB9G0x74cwMMRm2vUKgQARZECWBtya/m3919xokrd5ln6y7Hs3fLoQFwvx1nRordGGEMvzyGXZrHs3vbHO1cCG4E9YQFrixbrKSV8wjYed3crPbG8v40keQje+RL4i04kLCJ5De8poT/12Rpa7hvTJa8P2wtcE5bfouZ5iwe41zFbRNl+SWBLJFivxWNrwnKb2ty3l6D5PkfzeSRwr1rAwTfvIU+gI8LmEUVToyxKr33La3N/2HsCbxme8c5SgDPCAhKPGB2eeQPViiKluFbgo15v77HEd6yaKpT9WYgZANeN2vIzruwpwK6O6crzdI0IiIAIiIAIjCZAXqOipXqmgLm7UaRtWeGOFurK/aP15rISv/J51KvEK2Pc9ppR06FoLXlb0G8MfJS40dr2G2Pc9pneSteVMFxeQ96OXhRsC/qtgfOmiDDKitLdjfuwjKgmAiIgAiIgAiLQJkAxRKF1dNvynWsb45xnnF3Y0ILFnDq6vTo7PZLnuhjnPciUqJy7Rp/P/NNi3tFu1jNeKLAYEYnKcV426IX6BxsGy4hWYES/8++PD8axZtfJw6xksfokb11TY41KBERABERABERABERABERABERABERABERABERABERABERABERABFYh8D+KheQwB5Q5LQAAAABJRU5ErkJggg=="/></defs></svg>', 
    PROJ_TYPE_RATIONALE: f'<svg width="71" height="69" viewBox="0 0 71 69" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="71" height="69" fill="url(#pattern3)"/><defs><pattern id="pattern3" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image3" transform="translate(-0.00704225) scale(0.0084507 0.00869565)"/></pattern><image id="image3" width="120" height="115" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAABzCAYAAABTo8YRAAAE8UlEQVR4Ae2djbHVNhBGVUJKoARKSAmUQAkpgQ5SQkpICZRACZRACWROhp3xGHnldy24q+ujGY99/SudTyvtSnrQmkkCEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgATuQuCP1tpfrbXPrbUvrbWvP7Z/W2ufWmvv7gLi1cqJsH+31r611r4PNsTnftMiBP78YaUjYbfXqQjvFynfrbOJuGesdivu9vjjrekVLzz96RVxQ2gqiakggX8GfW0IONpTSUzFCNB/ZsIhGs4Ujhce9MjSb9NUE2KssGXWS3jUc6AQ+qhSEE6dLXexuv627Ixq+hGgKufJf0/coID4V/Ma71pyv7rANMlZ+qDA12v4VQu58vyoL8XzvvJ+nl06rW7B9KNZIiRS4AkQrkJ89Hn62CwxHv3ou+O57P3lr61uwYhAP9tLOF8zytd7t+cmE6CvDYvq7XG2wpuOGaZMXMIuUyECiJYJ1hM9O+dwZSFxIyszQh5E13qDaMF9NjqVWWxcwylzbrigsNss0d+GYG/ZI64rPLYkCx+PnK698K7qKCzmUdbwmrNJCERG2PCuj97j+QUI4IBh1TFDhJdsX7uAcGZRAhKQgASmEaDf06mZhrPGi3Bo8Fb3qydYFsPAxGjOtkYpzMVPBBB2L+o+/ozf3KfQPyGse4JwJMR7y340QV+3xDfK2aPiRkVQ5MKVZdaMztEkfeGi3yNrOFNhiVf2OGCmYgRG1ov4rIHiPpphRMwqgU7XbxCYwXpCmTNbJhhTeL2x32xqL8KoM99+5j2/QYZf94kZy2Cw3J64keuzoVRm7c+8FuVYcj9D4FFTe9Xrfqa4fHvpNEPgkUfM0OWzRbry/dsLPIprteAnVpEZFkwfm6VZodUVK7zybFa28tfwThHgzJZVBsKjXsqsl/ed+e6z7+mV6yXP4UxlloAlIyiTEPTLCJPdP2raXxJi5UIRCmWxcCbm/hrWm4VWlTm8dN5Go1l7IY9+j0Krl4ZYvXDZ6NSRoNvzPG8qTiBznrZi7o+PhjSLF/ee2WMAI/Ost+Jyn83yovUEa+6NN0cYxHUdqkXF3Wcbq45NUfd0/C0BCUhAAhJYmwB9O/18LA1iaNQ/7F5b0/9zj5AsMcpCMwdRFhQai0W4TNhtzM2xExmLCI24TGnuBTzz+2gKc5Giv342r4gbFUCRC9eT0b+/ESKO9qM1Y4URvG7WZv0HHIg/WlL0uhQLlyyzXpwtnChCJZpxLDS7H5Fva8Ws0ABYxa3X9JJPhO0lPO3eM3Hu0TL2vrXMOQodAFbYj5ymWUuKtiyWEbOX0dUEPrLeKNvIirfCnT2Ody+5X03g0ZAkffNZ4c7et6SwkenVBGa4MkuPDopkYmffK39tNYFZa32UZoZWW8GPvrfEeZyWilvmLBES7RN9c7bQHst+tJz7b/l7AgHE2FrR/pjBC4TmPoTNWiKujfruCVn2FW8hwADGXtRHf2O9poIEGH16VNR4jqaeymIqSmDUVIeQvT1N822HKIvq2c0WoVFPwOyc4nZR1j2Jl9xbXL8XGWFxunSq6mqZ5owml+HI8JwRNESlOVfYFJ8XJSABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAT6BP4DmxRqYwyJ6ZMAAAAASUVORK5CYII="/></defs></svg>', 
    PROJ_TYPE_DIRECT_COMMUNICATION: f'<svg width="63" height="61" viewBox="0 0 63 61" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="63" height="61" fill="url(#pattern4)"/><defs><pattern id="pattern4" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image4" transform="translate(-0.00517598) scale(0.0084196 0.00869565)"/></pattern><image id="image4" width="120" height="115" xlink:href="data:image/png;base64,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"/></defs></svg>',
    PROJ_TYPE_PERSUASIVE_PIECE: f'<svg width="71" height="69" viewBox="0 0 71 69" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="71" height="69" fill="url(#pattern5)"/><defs><pattern id="pattern5" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image5" transform="translate(-0.00704225) scale(0.0084507 0.00869565)"/></pattern><image id="image5" width="120" height="115" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAABzCAYAAABTo8YRAAAEe0lEQVR4Ae2dgY0TMRBFpwRKoARKoARKoARKoANKoARKoARKoARKAI2Ur+RG+2P7bll7//6VLJ8ns/b89725bKLLRfgwARMwARMwARMwARMwARMwARMwARMwARMwARMwARMwARMwARMwARMwARMwARMwgU4CvyPiiq0Tz/nT/kbEFdv5netUcEVzU/NlDhssbrUNtsGSv6PFbb3LY1fwh4hQaEzfnYD4T+oA1PU1t6c6AHV9Npjc5zfBqCSo73B1fc19qA5AXZ8N9lP09nvRzZ1xkgRfwYM7/GdErNjYfrPBgwYzYLPjNpgQYMaQ9GXfthytl+XLxW2wnKUvBY0a/CkiVmwvVd1Ho/ruZ4r8pA5AXV9zG6oDUNdngwfvEprAzpYwusN/RMSKjXEf1cfmOW18FADLnx1nBrC6WL5cfBQAy58dZ8awuli+XHwUAMufHWfGsLpYvlx8FMDniFixMWNG9bF5ThtXB6Cur7nx1AGo67PBvg8e+8D/W0Ss2NhO9hU8uMMZsNlxG0wIMGNIuj8PZmBWjdvgVZ3Zqa5Rg79ExIqN4RjVx+Y5bVwdgLq+5sZTB6CuzwYP3iU0gZ0tYeYO/xoRezXGfaY+VtOh8ZkA2NqviTNobC6WLxefCYCt/Zo4M4bNxfLl4jMBsLVfE2fGsLlYvlx8JoA939NmxszUx2o6NK4OQF1fc7OoA1DXZ4N9Hzz2eXBzxyyW4CtYfIfbYBu82HPOzuWo73B1fc3toA5AXZ8NFv8VZINt8Jq3Se8iIhs7nj32eI6fohfc4Wle/g1y/jeYLSMz9uv2fV2PZm79bIMXMzjN+/5QUzUZ5sK4/FK2Zwfyav/sHKnHqnCMZ4l8NBe15NWaxmbLKxtx9BljB3Jqz/Ll4lU4xrOEftwwMGtKk7fM/XP7c1ZWL/TUnuXLxatwjJnQvb4ji82fcWYyakPfMjfnQm7tn60v9VgVjjETicff2rP5EW+Z3GNuzsXqxDry/SgAlj8a7wGbzxZs3vzrip6Dnd9zrkTOKACWPxpvwWMvqLAOXni15kF+7VvnyTxehWPMBO71XdFs/oy3zEWNaXLrQG7tW+fJPF6FYzxLYK+5qLNlMvJqP0vf4etW4RgfXshtwa1boawpv9mHvfB69mYH9NR+lr7D163CMT68kNuC+e/0UAP6NBdHNTlfTeeLMXZgjtqzfLl4FY7xTKGPJj+ai5pgcsvczIee2mMu+b4Kx3i28DR5y1zUlSY/u3KRBz21x+PyfRWOsYpw6Km9ir6mjioc4+aJJ0mAntqfpPy3l1mFY/z2mdeYAXpqv0Z1B1RRhWN8wNKHLAE9tT9k8RUWqcIxXqG2PWqAntrvMfcp5qjCMT5F8R1FQk/tO07VSKnCMX4fEQoNemqv4V6Hiir8KuMONBopVzG06tRwr0NFFX6VcQcajZSrGFp1arjXoaIKv8q4A41GSn4ic8Wm4Z5VmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJmIAJ/F8C/wB/T/ZHNUmHxAAAAABJRU5ErkJggg=="/></defs></svg>', 
    PROJ_TYPE_PROMOTIONAL_CONTENT: f'<svg width="63" height="61" viewBox="0 0 63 61" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="63" height="61" fill="url(#pattern6)"/><defs><pattern id="pattern6" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image6" transform="translate(-0.00517598) scale(0.0084196 0.00869565)"/></pattern><image id="image6" width="120" height="115" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAABzCAYAAABTo8YRAAAEzUlEQVR4Ae2aD9HUMBBHIwEJSEACEpCABCTgAAlIQAISkICETwLMj2FnMjvNNUm3vW3uZabTa5umyXv51/RKIUAAAhCAAAQgAAEIQAACEIAABCAAAQhAAAIQgAAEIAABCEAAAhCAAAQgAAEIQAACEIAABCBwewLvSikf/m/vb18aCvCPwMdSytdSyq9Syp+N7Wcp5VspBeE3qzAS+2ND6JZkO7eKaPVSS1fYL6WUt0G5Jln3qXLcKUioyqzeqC73kpLVHZusI/vPiQ23hPryfkpchqmsqRb7Qh45FsgMoVeoL+tSgtUd1d2TL+zMsdK7OthMf6vLHS3DUoK/B7deg6ku/8wQKdTybPtlBKsLs0JF79WKJSEqnCnUl30ZwVETKw/Ijo9MuK4Uavm1/TKCf5/YggVL79O94ZlCTaztlxFsBTprvzXZ0rty/Z6pY/8eelZ+etNdQrAg9xZ4Np4XXA8JJrk+N/uc6PsQPFA56olWvQRq4zOCewexwXgCH13zfXoa4+uA4JrGBb+9kOhjfYmqA4JrGhf8bn0KjBKtr0x1QHBN44Lf0WvQvmL4yQqCL5BaP+LMcVjjbz3B0nMRXNO/6PdZa9HqHXxQl22t3Fo3s2hPKfhYrSx6RUsLF771Ktta+9a4X19HcLDQreQiPzqostgixtaz/Dm9D1urzrK33sXn9dbHWjI8ClhyVVlmgp6vbr0ep4/mZ/b+JQVLiuTMdtfqdkda7l4lkPBnyV5WsEEfeX1ShVD8rTHX0pvdC7S1QglXd66Jmta47fwZ++UFmxAVVLNstU6JFFjtNVESaLX4M8Ta85W2CbS16/qaCY9esHkZwQbzWXsJttZqlao1DCiuxMwOMVaRtEfwBcYF2eTW8PVbvYeu+96jHlosjl7DRls4gk8WXIvycv2xWqxk6h6rEBpWtoLE9Qh/KcHW9QmgNgHShKfVVW6BHTk3ItfL1rFaq2/Zree3hKt8SwcB0gRmr2vTdQmPCqNyrcJpEqjWW6+QzeRJwmff42ee95R7VHv3xPqWI7h+ljua+VG5ysPyMkYh7sU/+uGhNfbtPXdGLoL3qLrrmqj4ljlzrG5yJMzKHX3OSJ6Wi6txdEZm6x5J6wmzcvXc5SdCPQB74mg2bK8XLWEz5/cEHJGr3obQSeDouNuSr4laKyC3RSb4vFpZS1DEeaWvV656Q26wxEfJRU2sIirDXhp0y49MNq4963vrnkx/HbkNgXunI768eBnRx8jds9i4rtlztIzo9JDbkNdzOrtg5PZYfBAns2DkPhDXeymrYOT2GtyJl1EwcnekjVzOJhi5I/Y64mYRrHXwl/qLTIebkChXCdaXKi1Pbm1n/+02BNRdE7lKcO//o+7KMW2+EZxWTUzGEBzDMW0qCE6rJiZjCI7hmDYVBKdVE5MxBMdwTJsKgtOqickYgmM4pk0FwWnVxGQMwTEc06aC4LRqYjKG4BiOaVNBcFo1MRlDcAzHtKkgOK2amIwhOIZj2lQQnFZNTMYQHMMxbSoITqsmJmMIjuGYNhUEp1UTkzEEx3BMm4r+zqo/nJ+9pQVAxiAAAQhAAAIQgAAEIAABCEAAAhCAAAQgAAEIQAACEIAABCAAAQhAAAIQgAAEIAABCEAAAhBISuAvRSPsnDRoF3MAAAAASUVORK5CYII="/></defs></svg>', 
    PROJ_TYPE_BUSINESS_PROPOSAL: f'<svg width="71" height="69" viewBox="0 0 71 69" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="71" height="69" fill="url(#pattern7)"/><defs><pattern id="pattern7" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image7" transform="translate(-0.00722758) scale(0.00852483 0.00877193)"/></pattern><image id="image7" width="119" height="114" xlink:href="data:image/png;base64,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"/></defs></svg>',
    PROJ_TYPE_REQUIREMENTS_DOCUMENT: f'<svg width="63" height="61" viewBox="0 0 63 61" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="63" height="61" fill="url(#pattern8)"/><defs><pattern id="pattern8" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image8" transform="translate(-0.00517598) scale(0.0084196 0.00869565)"/></pattern><image id="image8" width="120" height="115" xlink:href="data:image/png;base64,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"/></defs></svg>', 
    PROJ_TYPE_FUTURE_SCENARIO: f'<svg width="57" height="56" viewBox="0 0 57 56" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="57" height="56" fill="url(#pattern9)"/><defs><pattern id="pattern9" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image9" transform="translate(-0.131129 -0.107143) scale(0.0103464 0.0105311)"/></pattern><image id="image9" width="122" height="117" xlink:href="data:image/png;base64,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"/></defs></svg>', 
    PROJ_TYPE_TECHNICAL_DOCUMENT: f'<svg width="63" height="61" viewBox="0 0 63 61" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="63" height="61" fill="url(#pattern10)"/><defs><pattern id="pattern10" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image10" transform="translate(-0.00536062) scale(0.00849346 0.00877193)"/></pattern><image id="image10" width="119" height="114" xlink:href="data:image/png;base64,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"/></defs></svg>',
    PROJ_TYPE_TRAINING_PROGRAM: f'<svg width="71" height="69" viewBox="0 0 71 69" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="71" height="69" fill="url(#pattern11)"/><defs><pattern id="pattern11" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image11" transform="translate(-0.00704225) scale(0.0084507 0.00869565)"/></pattern><image id="image11" width="120" height="115" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAABzCAYAAABTo8YRAAAEW0lEQVR4Ae2bC9HUMBgAIwEJSEACEpCABCTgAAlIQAISkIAEJMDszJ+Z0mmul1za5Gu3M53eq02zm3x5NJeSmwQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQuS+BjSulbSumX+38MfrxxeR/Z/PeU0l/3XQafIkr+othdsbnw/0kphavJhKCcAY/7LKgQobbfCq4q4F9D2U0pEXasuc8zoCMaaisJ/vnWeyRDd9xLXC4jOFxb07laMVzcimwK7gx61OUUPIr8Sekq+CTQo5JR8CjyJ6Wr4JNAj0pGwaPIn5Sugk8CPSoZBY8if1K6Cj4J9KhkFDyK/EnpKvgk0KOSuYxgHirkZSnMP39OKfFI7MMospOkexnBk/Cc7jYUPJ2Svjek4L48p7vapQS/SymxbJZVg7TBvL77dgnBiGXJbGn1At+FW0XYqWSGF0xNLYldr2Tgt3fbQgtm2cla4t77uy3hCSuYdnZPZun7O7XNIQXT5pZuvCR1+Tkh/S5bidPUi+4Is0thLa97h+r8pzcW4AMVgDN07EIK7vE3Fa7Rayt19IgUo6dKQwru8TeVXmGamvuoF98rndbCGFJwS0jeOqcVWj6P2vlIbk5zZKcupOBnoGa4pSNR4JXtWbmkP3L8HVJwjxBNxlu3GrkIHvmH65CCWyY41jW59e+TtXIpjAzrRm0hBTP8WAureU+IR1Ttxjk10YN0RtZe8hdSMDf+yli4ZQxMoaqVO7LtzYU3rOBHpfNRbW4Z/9bKJf0Z5D5iNPVMVi6d+THhI6HL73hsWNsetkyLtkSInKfex9A1OMMozSRlua1tYYvc1s5bzkvv4yUEZyh0aABMTWUnDNExqq21XI9zaqdEZwx7lxKcRb96vIpcOFxSMIJaau2Vam4u5KEFE37p0BCOyQjDmPU0Jp/xHeGW8E0YL8lvrbml62XII4/hBDNkQVTNmDR3tpZHhC+HMi1yW3rlZ8sOIRj4PJHhZtc1dCmt5TUFhc4RsmrO568yWzWXz2bapxeM2Fdra424Z34LtC25NBe9C+Az99Pym+E9fgByEy03f+Q5Jbl7Y/Ej76nl2kMFz1hrgViSy/1Gqbm5MAybkJkVFnLp4K03evLR5CJ52FOu2dpbYCDwSnJbHrisC3bTe0pVDiGzHJG7Vdqj1tyhQzvahVnE5vtYjpWXpRbBiI+y0/RtRaFlng5/XTu5nyUcdRza0zyc9skJMCyaqbOi3M4FgBByVE2svW5plqpzlu91OWaBakUc8fvSWPdeNg7I7Qztb2k4dEB273fJ0ePf0nDofiYOyDFDjiPCbc01t8a6B2T1npcELm3fqH2mVZD3LAHmWgISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQnsEvgHJPxN09t1bcEAAAAASUVORK5CYII="/></defs></svg>',
}



PROJ_TYPE_SUBTYPES = {}

for pt in PROJ_TYPE_LIST:
    PROJ_TYPE_SUBTYPES[pt] = ' / '.join([i[1].lower() for i in PROJ_SUBTYPE_CHOICES_SEL[pt]])


PROJ_TYPE_DESCRIPTIONS = {
    PROJ_TYPE_ANALYSIS_REPORT: 'Provides a structured framework for assessing something and documenting a report to communicate the findings. Leverages best practice methods in critical thinking',
    PROJ_TYPE_COMPLIANCE_DOCUMENT: 'A compliance document outlines how staff, contractors or third parties should act. Incorporates external 3rd party requirements such as government legislation and applies them to an organisational context. Available in MS Word/Google Docs/Pdf/Text. Outputs available from 5 pages to 100 pages. Deliverable contains introduction, table of contents, and numbered headings and sections. Logo and 3 customisable images available.',
    PROJ_TYPE_CREATIVE_CONTENT: 'Creative content is a work that is designed to delight and entertain. Content not based purely on analysis, uses ideas (unexpected connections) to "present with identity", enabling the content to be highly differentiated. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 500 pages. Deliverable is presented in topic order, does not contain table of contents or summary, designer template with no logo and scope for two custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_RATIONALE: 'A rationale is a document that uses Pyramid Thinking to identify and support a conclusion or recommendation. Helps the user to understand implications and choose between alternatives based on their personal or organisational situation. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 100 pages. Deliverable contains introduction, table of contents executive summary, conclusion and summary. Customisable images include one logo plus three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_DIRECT_COMMUNICATION: 'A piece of communication designed to communicate a specific message to one or more readers in a direct (not broadcast) communication. Available in a range of formats suitable for each communication type (Text for Email), and MS Word/Google Docs/Pdf for Newsletters and Memos - Outputs available in 1-10 pages. Deliverable contains appropriate formatting and content for your chosen document type. Word document outputs include images - one logo plus three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_PERSUASIVE_PIECE: 'A persuasive/explanatory piece of writing on a particular subject (Non Fiction) that is designed to persuade a business or individual about either the benefits or implications of something. Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text - Note multiple outputs availabe from a single consultation between 1 page and 50 pages. Deliverable is presented to maximise the structuring and presentation of arguments to lead the reader to a clear conclusion. Contains a table of contents, summary, designer template scope for custom logo and three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_PROMOTIONAL_CONTENT: 'Promotes a business, concept or idea. This content is designed to be used in marketing communication and broadcast to your prospective target audience. Available in HTML/XML/MS Powerpoint/MS Word/Goole Docs/Google Slides/Pdf/Text - Note some promotional work document categories provide a zipped folder of documents such as landing page and website. Format makes providsion for specified document format. Can be future, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_BUSINESS_PROPOSAL: 'A business document that assists you to identify, define and communicate a suggested future state, relationship or structure. Designed to elicit approval by a 3rd party. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 100 pages. Deliverable contains introduction, table of contents executive summary, conclusion and summary. Customisable images include one logo plus three custom images. Can be future, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_REQUIREMENTS_DOCUMENT: 'A business document that to identify and communicate business or project requirements to another individual or organisation. Available in MS Word/Google Docs/Pdf/Text - Outputs available from 1 page to 100 pages - landscape or portrait format. Deliverable contains introduction, table of contents executive summary, conclusion and summary. Customisable images include one logo plus three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_FUTURE_SCENARIO: 'Develops a clear picture of a future scenario that does not yet exist and positively presents this to the reader. Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text - Note multiple outputs availabe from a single consultation between 1 page and 100 pages. Landscape and Portrait options available. Method used facilitates the development of a logically consistent future scenario. Contains a table of contents, summary, designer template scope for custom logo and three custom images. Can be future, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_TECHNICAL_DOCUMENT: 'Outlines to the user of a product or service how to use that product or serviced. Available in MS Word/Google Docs/Pdf/Text. Outputs available from 5 pages to 100 pages. Presented in portrait format. Deliverable contains introduction, table of contents, and numbered headings and sections. Logo and 3 customisable images available. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
    PROJ_TYPE_TRAINING_PROGRAM: 'Content that is designed to train someone or teach someone how to do something - typically designed to be presented by a teacher, tutor etc. Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text - Note multiple outputs availabe from a single consultation between 1 page and 100 pages. Landscape and Portrait options available. Method used facilitates the clear structuring of concepts for communication to those who are in a learning mode. Contains a table of contents, summary, designer template scope for custom logo and three custom images. Can be present, explanatory, explanatory MethodX, docTemplateX, icon Y',
}

PROJ_TYPE_OUTPUT_DETAILS = {
    PROJ_TYPE_ANALYSIS_REPORT: 'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 1 page to 100 pages - portrait format.  Includes: introduction, table of contents executive summary, conclusion and summary.  Offers 4 customisable images including logo.',
    PROJ_TYPE_COMPLIANCE_DOCUMENT: 'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 5 pages to 100 pages.  Deliverable contains introduction, table of contents, and numbered headings and sections.  Logo and 3 customisable images available.',
    PROJ_TYPE_CREATIVE_CONTENT: 'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 1 page to 500 pages.  Deliverable is presented in topic order, does not contain table of contents or summary, designer template with no logo and scope for two custom images.',
    PROJ_TYPE_RATIONALE: 'Available in MS Word/Google Docs/Pdf/Text.  Outputs available from 1 page to 100 pages.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.',
    PROJ_TYPE_DIRECT_COMMUNICATION: 'Available in a range of formats suitable for each communication type (Text for Email), and MS Word/Google Docs/Pdf for Newsletters and Memos -  Outputs available in 1-10 pages.  Deliverable contains appropriate formatting and content for your chosen document type.   Word document outputs include images - one logo plus three custom images.',
    PROJ_TYPE_PERSUASIVE_PIECE: 'Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs available from a single consultation between 1 page and 50 pages.  Deliverable is presented to maximise the structuring and presentation of arguments to lead the reader to a clear conclusion. Contains a table of contents, summary, designer template scope for custom logo and three custom images.',
    PROJ_TYPE_PROMOTIONAL_CONTENT: 'Available in HTML/XML/MS Powerpoint/MS Word/Goole Docs/Google Slides/Pdf/Text - Note some promotional work document categories provide a zipped folder of documents such as landing page and website.  Format makes providsion for specified document format.',
    PROJ_TYPE_BUSINESS_PROPOSAL: 'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 1 page to 100 pages.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.',
    PROJ_TYPE_REQUIREMENTS_DOCUMENT: 'Available in MS Word/Google Docs/Pdf/Text.  Outputs available from 1 page to 100 pages - landscape or portrait format.  Deliverable contains introduction, table of contents executive summary, conclusion and summary.  Customisable images include one logo plus three custom images.',
    PROJ_TYPE_FUTURE_SCENARIO: 'Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs availabe from a single consultation between 1 page and 100 pages.  Landscape and Portrait options available.  Method used facilitates the development of a logically consistent future scenario.  Contains a table of contents, summary, designer template scope for custom logo and three custom images.',
    PROJ_TYPE_TECHNICAL_DOCUMENT: 'Available in MS Word/Google Docs/Pdf/Text.  Outputs - 5 pages to 100 pages.  Presented in portrait format.  Deliverable contains introduction, table of contents, and numbered headings and sections.  Logo and 3 customisable images available.',
    PROJ_TYPE_TRAINING_PROGRAM: 'Available in MS Powerpoint/MS Word/Google Docs/Google Slides/Pdf/Text  - Note multiple outputs availabe from a single consultation between 1 page and 100 pages.  Landscape and Portrait options available.  Method used facilitates the clear structuring of concepts for communication to those who are in a learning mode.  Contains a table of contents, summary, designer template scope for custom logo and three custom images.',
}

PROJ_DOCSIZE_DESCRIPTIONS = {
    PROJ_DOCSIZE_1: 'Small document or overview - covers one master topic and 3 subtopics.  Wordcount from 200 words to 500 words depending on output format.',
    PROJ_DOCSIZE_UPTO_5: '5 page document, a brief document typically covering one master topic, 3 subtopics and 2 further subtopics.  Wordcount 1,000 to 2,000 words depending on output format.',
    PROJ_DOCSIZE_UPTO_20: '20 page document, a signficant document with master topics and subtopics dynamically assembled throughout the process - typically a 4 level topic heirarchy.  Wordcount 4,000 to 7,000 words depending on output format.',
    PROJ_DOCSIZE_UNLIMITED: 'Unlimited size - eg book. Provides a substantial volume of content that includes numerous topics and subtopics.  Output will be largely text.',
}

PROJ_SUBTYPE_DESCRIPTIONS = {
    PROJ_TYPE_ANALYSIS_REPORT: {
        PROJ_SUBTYPE_ASSESSMENT: 'States a position or Hypothesis and breaks that position down into a number of supporting and dissenting view ultimately providing a rounded evaluation of a topic and usually presenting a recommendation.',
        PROJ_SUBTYPE_REVIEW: 'Evaluates the performance, features or benefits of something or someone and leaves the reader with an impression (a positive or negative feeling) related to the topic.',
        PROJ_SUBTYPE_REPORT: 'Documents the findings that have resulted from the analysis of a core topic or objective and outlines the reasoning behind those findings.',
        PROJ_SUBTYPE_COMPARISON: 'This document type makes a comparison between one or more people, places, things or groups. It is designed to compare and contrast different features, benefits or aspects.',
    }, 
    PROJ_TYPE_COMPLIANCE_DOCUMENT: {
        PROJ_SUBTYPE_POLICY_DOCUMENT: 'Offers a structured approach to presenting an organisations policies to staff, suppliers, customer or members. The document is clearly structured around legal or organisational objectives and is designed to make the reader able to assess if they are in compliance or not in compliance with policies.',
        PROJ_SUBTYPE_PROCEDURES_DOCUMENT: 'Outlines step by step activities that are required to achieve either compliance or a desired organisational objective.',
    },
    PROJ_TYPE_CREATIVE_CONTENT: {
        PROJ_SUBTYPE_CREATIVE_FICTION: 'Not based on fact, but interesting presents a series of plausible hypotheticals. Not presented in a chronological manner.',
        PROJ_SUBTYPE_CREATION_NON_FICTION: 'A unique method for exploring non-fiction topics and drilling down into aspects of potential interest to the reader.',
    }, 
    PROJ_TYPE_RATIONALE: {
        PROJ_SUBTYPE_DECISION_RATIONALE: 'Outlines the basis on which a decision is made or recommended, evaluates various benefits, features and aspects against objectives.',
        PROJ_SUBTYPE_SELECTION_ANALYSIS: 'Provides reasoning behind the selection of one of several different options (usually three options are defined and assessed).',
        PROJ_SUBTYPE_RECOMMENDATION: 'Outlines why a particular course of action is recommended. This can relate to a product, service, organisation or strategic initiative. It can also provide clarification of a proposed course of action for significant personal matters.',
    }, 
    PROJ_TYPE_DIRECT_COMMUNICATION: {
        PROJ_SUBTYPE_EMAIL: 'An electronic communication usually between one individual and another, although can be sent to groups of individuals. Usually has a specific and targetted message.',
        PROJ_SUBTYPE_LETTER: 'Usually a one or two-page personal communication, either sent as an attachment in an email or printed and posted. It is one of the more personal forms of communication for both business and personal communication.',
        PROJ_SUBTYPE_MEMO: 'Used by organisations for internal communications although can be part of stakeholder or investor relations processes. A memo typically documents and communicates a memorandum of understanding.',
        PROJ_SUBTYPE_NOTICE: 'Provides new information to the reader about a topic that might affect them. Notices are a core aspect of stakeholder communications processes.',
        PROJ_SUBTYPE_NEWSLETTER: 'A method of communicating multiple points to a largely homogenous group of individuals. It is often used in business or by sporting clubs to maintain membership and engagement.',
    },
    PROJ_TYPE_PERSUASIVE_PIECE: {
        PROJ_SUBTYPE_ESSAY: 'A short formal piece of writing, usually for educational purposes to demonstrate knowledge of a topic or explore a topic.  It contains an introduction, body and conclusion and is usually a maximum of 5,000 words.',
        PROJ_SUBTYPE_ARTICLE: 'An expose on a topic, articles are often used for online "content marketing" typically being between 400 words and 1,500 words in length.',
        PROJ_SUBTYPE_BLOG_POST: 'A blog post is similar in nature to an article although is often shorter and specifically targets a feature, benefit or pain point directly.',
        PROJ_SUBTYPE_E_BOOK: 'A short-form book designed to be consumed by an e-reader.  Ebooks are often used as a free or low-cost introduction to a topic, product or service.  Our ebook format is output with images in PDF format and you may later need to popular ebook formats.',
        PROJ_SUBTYPE_BOOK: 'A book is a detailed explanation on a topic and can run to many hundreds of pages.  In a book key topics or areas are often referred to as chapters.  Our book format contains text and has very limited scope for images and is delivered in MS Word and PDF formats.',
        PROJ_SUBTYPE_WHITEPAPER: 'Aan informational document, usually issued by a company or not for profit organisation to promote or highlight features of a solution, product or service.  Often associated with the introduction of new technology.',
    }, 
    PROJ_TYPE_PROMOTIONAL_CONTENT: {
        PROJ_SUBTYPE_WEBSITE: 'A series of inter-related web pages usually associated with a domain.  A website is similar to an online brochure that presents information about a company, product, service or cause.  A website can be a minimum of 3 web pages.',
        PROJ_SUBTYPE_LANDING_PAGE: 'A single-page website used to drive conversion online.  Conversions can relate to capturing leads, obtaining bookings or selling a product or service.',
        PROJ_SUBTYPE_ADVERTISEMENT: 'As used here relates typically to a full-page advertisement in a newspaper or magazine.  It is intended multiple advertisement output formats will be developed including online display, online search, and offline.',
        PROJ_SUBTYPE_FLIER: 'A form of advertisement intended for wide distribution either via printed copy or via attachment in electronic communication.  A flier is typically one to four pages in length and integrates imagery and design.',
        PROJ_SUBTYPE_BROCHURE: 'Typically a glossy image-centric communication used by organisations to promote a product, service or concept.  Brochures are typically one to ten pages in length.',
    }, 
    PROJ_TYPE_BUSINESS_PROPOSAL: {
        PROJ_SUBTYPE_PROPOSAL: 'A future-oriented document.  It relates to stating a written offer to a prospective buyer.  This format is suitable for proposals, requests for information and tender responses where the format is not specified.  Ideally suited to complex services proposals.  If the required format is specified by the prospect then some cutting and pasting may be required.',
        PROJ_SUBTYPE_QUOTE: 'Typically a one or two-page (brief) proposal.  It is typically less convincing than a proposal but for small product or services sales is sufficient as the basis of a transaction.',
        PROJ_SUBTYPE_POTENTIAL_SCENARIO: 'A potential scenario relates to explaining what a future scenario may look-like, and providing a rationale for your views.',
    },
    PROJ_TYPE_REQUIREMENTS_DOCUMENT: {
        PROJ_SUBTYPE_SCOPE: 'Outlines the boundaries of a project (in-scope and out of scope).  Scope documents are most often used in large services-based projects and can range from one page to 10 pages in length.',
        PROJ_SUBTYPE_CHARTER: 'Outlines the objectives and boundaries associated with a venture, organisation or program.',
        PROJ_SUBTYPE_BUSINESS_REQUIREMENTS_DOCUMENT: 'Outlines the requirements of a business or business unit in relation to the development of a new product, service or piece of software.',
    }, 
    PROJ_TYPE_FUTURE_SCENARIO: {
        PROJ_SUBTYPE_STRATEGY: 'A strategy, often referred to as a strategic plan is briefer than a business plan.  It focuses on defining a high-level future pathway and providing a rationale for the recommended goals, objectives and vision.',
        PROJ_SUBTYPE_PLAN: 'Includes plans such as business plan, marketing plan, investment plan, human resources plan etc.  In words outlines the strategy and structure behind achieving a future-oriented objectives, and is designed as a sales document to convince and provide confidence in the achievement of the plan.',
        PROJ_SUBTYPE_GOAL_OUTLINE: 'Typically one page and outlines key business goals and why they are important to the organisation.',
        PROJ_SUBTYPE_DEFINITION_DOCUMENT: '??? MISSING',
    }, 
    PROJ_TYPE_TECHNICAL_DOCUMENT: {
        PROJ_SUBTYPE_HOW_TO_ARTICLE: 'Describes to the target reader how to do something.  It is effectively a mini-product manual or guide that provides step-by-step guidance.',
        PROJ_SUBTYPE_PATENT_SPECIFICATION: 'A document that is designed to be used as part of a patent application.  It is not the full patent but is often referred to as the abstract and can stretch from one page to three pages in length.',
        PROJ_SUBTYPE_PRODUCT_MANUAL: 'A product manual is the type of printed or electronic document that accompanies the purchase of a product (Eg. a vehicle, computer or smartphone.  The manual covers all significant areas of usage.',
    },
    PROJ_TYPE_TRAINING_PROGRAM: {
        PROJ_SUBTYPE_CURRICULUM: 'Relates to the development of course materials for students and often comprises of multiple classes and topics.',
        PROJ_SUBTYPE_TRAINING_DOCUMENT: 'A step by step guide on what needs to be learned and accompanies either teaching materials or is used for train the trainer activities.',
    },
}

PROJ_TOPIC_DESCRIPTIONS = {
    PROJ_TOPIC_PERSON: 'A person is typically one named individual who will be at the centre of your document. Effectively the entire document will be about them.',
    PROJ_TOPIC_COMPANY: 'A company is a legal entity designed either for-profit.  An organisation is typically either a government agency or not-for-profit organisation.  Consider carefully when selecting a company or organisation that you are referring to the legal title of the organisation and not a division within an organisation.',
    PROJ_TOPIC_GROUP: 'A group is a named group of people, things or animals.  It could also be a division with a company or organisation, For example, a local football team is a group, elephants are a group of animals etc.',
    PROJ_TOPIC_PRODUCT_SERVICE: 'A product is a tangible item that is put on the market for acquisition, attention, or consumption, while a service is an intangible item, which arises from the output of one or more individuals.',
    PROJ_TOPIC_CONCEPT_THING: 'This category relates to ideas and abstract concepts.  Examples include - climate - technology - flying.  Furthermore, this category also includes things these may be products such as - Lego - Computers - Boeing A380.',
    PROJ_TOPIC_PLACE_DEST_BUILDING: 'A place, destination or building is a physical area that can be seen on a map or satellite photograph.  If you are referring to a group of places (eg Parks) then group would be a better selection.',
}

def getChoiceHeading_doc_subtype(project):
    return "What sort of " + PROJ_TYPE_LIST[project.doc_type] + " would you like to start creating?"

def getChoiceHeading_doc_topic(project):
    prop_target_reader_exp = project.props.get(name=PROP_TARGET_READER).response_exp
    return "What is the main subject or topic you would like to cover in this " + PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower() + " for " + prop_target_reader_exp + "?"


def getChoiceHeading_doc_len(project):
    return "Thanks " + project.creator.first_name + ", I now have a much better understanding of what you are looking to do. <br> How long (approximately) would you like your " + PROJ_TYPE_LIST[project.doc_type].lower() + " to be?"

def getPropQuestionText(project, p_name):
    if p_name == PROP_TARGET_READER:
        return project.creator.first_name + ", who (what individual or group) will be reading your " + PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower() + "?"
    elif p_name == PROP_TOPIC_NAME:
        return "What is the name of the " + PROJ_TOPIC_CHOICES_LIST[project.doc_topic].lower() + " you would like to cover in this " + PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower() + "?"
    elif p_name == PROP_TOPIC_IMPACT:
        return "Who or what is most " + "impacted by the " + PROJ_TOPIC_CHOICES_LIST[project.doc_topic].lower() + " - '" + project.props.get(name=PROP_TOPIC_NAME).response + "'?"
    elif p_name == PROP_TARGET_IMPRESSION:
        prop_target_reader_exp = project.props.get(name=PROP_TARGET_READER).response_exp
        prop_topic_name_exp = project.props.get(name=PROP_TOPIC_NAME).response_exp
        return "What action or impression do you want " + prop_target_reader_exp + " to have as a result of reading this " + PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower() +" on " + prop_topic_name_exp + "?"
    elif p_name == PROP_TOPIC_CAUSE:
        prop_topic_name_exp = project.props.get(name=PROP_TOPIC_NAME).response_exp
        return "Who or what is affecting, causing or creating " + prop_topic_name_exp + "?"
    return '?'

def getPropQuestionLeadIn(project, p_name):
    if p_name == PROP_TARGET_READER:
        return "My " + PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower() + " is ultimately for :  "
    elif p_name == PROP_TOPIC_NAME:
        return "The main subject or topic for this " + PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower() + " will be a..."
    elif p_name == PROP_TOPIC_IMPACT:
        prop_topic_name_exp = project.props.get(name=PROP_TOPIC_NAME).response_exp
        return prop_topic_name_exp[0].upper() + prop_topic_name_exp[1:] + " will have the greatest " + "impact on..."
    elif p_name == PROP_TARGET_IMPRESSION:
        prop_target_reader_exp = project.props.get(name=PROP_TARGET_READER).response_exp
        return "I would like " + prop_target_reader_exp + " to...  "
    elif p_name == PROP_TOPIC_CAUSE:
        prop_topic_name_exp = project.props.get(name=PROP_TOPIC_NAME).response_exp
        return prop_topic_name_exp[0].upper() + prop_topic_name_exp[1:] + " will be impacted by...  "
    return '?'

def getDocBasecampTopText(project):
    return f'{project.creator.first_name}, you have reached Document Basecamp'

def getDocBasecampSubText(project):
    return PROJ_TYPE_LIST[project.doc_type] + " brief:"

def genBasecampPropEditFieldHTML(prop, sentence_start=False):
    if sentence_start:
        return f"<span class='editable' pname=\'{prop.name}\' pvalue=\'{prop.response}' evalue=\'{prop.response_exp}\' tvalue=\'{prop.response_exp[0].upper()}{prop.response_exp[1:]}\'>{prop.response_exp[0].upper()}{prop.response_exp[1:]}</span>"
    else:
        return f"<span class='editable' pname=\'{prop.name}\' pvalue=\'{prop.response}' evalue=\'{prop.response_exp}\' tvalue=\'{prop.response_exp}\'>{prop.response_exp}</span>"

def getDocBasecampResponsesList(project):
    # doc_type
    chosenDoctype = PROJ_TYPE_LIST[project.doc_type].lower()
    # doc_subtype expression
    detailedDoctypeSelected = PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower()
    dde = q_what(detailedDoctypeSelected)[-1]
    # prop:PROP_TARGET_READER expression
    prop_target_reader = project.props.get(name=PROP_TARGET_READER)
    prop_target_reader_exp = prop_target_reader.response_exp
    # prop:PROP_TOPIC_NAME expression
    prop_topic_name = project.props.get(name=PROP_TOPIC_NAME)
    prop_topic_name_response = prop_topic_name.response
    # prop:PROP_TOPIC_NAME plurarity
    subjectExpressionWhat = q_what(prop_topic_name_response)[2]
    sEWPlural = ""
    if subjectExpressionWhat.find("are") == 0:
        sEWPlural = "s"
    # prop:PROP_TARGET_IMPRESSION expression
    prop_target_impression = project.props.get(name=PROP_TARGET_IMPRESSION)
    # prop:PROP_TOPIC_IMPACT expression
    prop_topic_impact = project.props.get(name=PROP_TOPIC_IMPACT)
    # document orientation
    selectedOrientationText = getAutoOrientation()
    # basecamp responses text
    p11header = f"The way I see it, {project.creator.first_name}, is that you are looking to develop {dde} that will be read primarily by {genBasecampPropEditFieldHTML(prop_target_reader)}." 
    p11header = p11header + f" {genBasecampPropEditFieldHTML(prop_topic_name, True)} {subjectExpressionWhat} the primary subject{sEWPlural}/topic{sEWPlural} that will be covered in this {chosenDoctype}." 
    p11header = p11header + f" The main goal of this document is for {prop_target_reader_exp} to {genBasecampPropEditFieldHTML(prop_target_impression)}."
    p11body = f"This document will clearly and succinctly communicate how {prop_topic_name_response} will impact {selectedOrientationText} on {genBasecampPropEditFieldHTML(prop_topic_impact)}."
    return f"<p>{p11header}</p><p>{p11body}</p><p>Ok let's go.</p>"


pwoLists = [['Please select'],["impact","improve", "strengthen","progress", "develop", "elevate", "upgrade", "help", "assist", "enhance", "better", "advance", "refine", "amplify"],["impact", "diminish", "reduce", "lessen","minimise", "lower", "decrease", "disturb","impinge on","upset"],["impact", "change", "affect", "influence", "transform", "alter", "shift"]]
primaryOrientation = ['Please Select...', "positively", "negatively", "neutrally"]

def getAutoOrientation():
    selectedOrientation = -1
    proposalWordsOutcome = pwoLists[selectedOrientation]
    proposalWordsOutcomesPossibilities = {}
    for el in proposalWordsOutcome:
        proposalWordsOutcomesPossibilities[el] = []
        for i in range(3):
            global lemm
            lemm = el
            if(i == 0) :
                doc = nlp(el)
                for token in doc:
                        lemm = token.lemma_
                proposalWordsOutcomesPossibilities[el] .append(lemm)
            if(i == 1) :
                if(el[-1] == 'e'):
                    lemm = el + "d"
                elif(el[-1] != "e") :
                    lemm = el + "ed"
                proposalWordsOutcomesPossibilities[el] .append(lemm)
            if(i == 2) :
                if(el[-1] == "e") :
                    lemm = el[0:len(el) - 1] + "ing"
                else :
                    lemm = el + "ing"
                proposalWordsOutcomesPossibilities[el] .append(lemm)
    return primaryOrientation[selectedOrientation]

# page tips
def getTip_title():
    return "<p>Name your project something that will help you identify it.</p>\
            <p>Note that with Hyper Questions, we will use your name throughout your document so pick something that also reads well.</p>"

def getTip_doc_type():
    return "<p>Once you select an option, a description of this type and its output formats will be displayed – this will help you be sure you have picked the best option.</p>\
            <p>Please consider carefully as each type may produce different outcomes – select one and see what it offers.</p>"

def getTip_doc_sutype(project):
    return "<p>These are sub-options associated with your selection of " + PROJ_TYPE_LIST[project.doc_type] + ".</p>\
            <p>Once you select an option further information about its method and approach will be displayed.</p>"

def getTip_doc_topic():
    return "<p>Select your subject/topic type from the given table, try for a best-fit approach if your topic crosses several types.</p>"

def getTip_doc_len():
    return "<p>Document length is approximate and will be used to determine the number of topics and questions required.</p><p>Actual length is dependent on several factors including: document format, answer length and the number of skipped questions.</p>"

def getTip_prop(project, p_name):
    if p_name == PROP_TARGET_READER:
        return "<p>This is your target reader – it can be an individual (e.g. Nicholas Tesla), a group (e.g. board of directors), a company (e.g. Microsoft), an industry or sector (e.g. manufacturing).</p>\
                <p>Please use correct capitalisation and resist responses like 'everyone'... you may need to think specifically about who will be the target reader.</p>"
    elif p_name == PROP_TOPIC_NAME:
        return "<p>This is the main/primay subject in your document. Think carefully about this as it will impact everything you do from now on.</p>\
                <p>You may not get it right at this time, and may need to come back and revise it once you see it presented in other contexts.</p>"
    elif p_name == PROP_TOPIC_IMPACT:
        prop_target_reader_exp = project.props.get(name=PROP_TARGET_READER).response_exp
        prop_topic_name_exp = project.props.get(name=PROP_TOPIC_NAME).response_exp
        return f"<p>Think of this in the context of your document – what you are trying to say about {prop_topic_name_exp}.</p><p>This can be a: person, division within an organisation, organisation/entity, place, product concept etc.  It could also be the target reader of your document ({prop_target_reader_exp}).</p><p>Try to separate from target reader if possible e.g. if target reader is board of a company, those affected could be the staff.</p>"
    elif p_name == PROP_TARGET_IMPRESSION:
        prop_target_reader_exp = project.props.get(name=PROP_TARGET_READER).response_exp
        return "<p>Example: I would like " + prop_target_reader_exp + " to... (buy our product, visit our website, make x decision, feel informed, become more engaged etc).</p>"
    elif p_name == PROP_TOPIC_CAUSE:
        prop_target_reader_exp = project.props.get(name=PROP_TARGET_READER).response_exp
        prop_topic_name_exp = project.props.get(name=PROP_TOPIC_NAME).response_exp
        return "<p>This is ideally something or someone that is driving change in " + prop_topic_name_exp + ".</p><p>It could be a person, team (e.g. marketing), regulation, place, product concept etc.</p><p>If you really get stuck, don't worry just use " + prop_target_reader_exp + ".</p>"
    return ""

def getTip_basecamp():
    return "<p>Please take a moment to review your responses thus far - it will make the rest of this journey much easier.</p>\
            <p>If you see any issues, go back to correct now (it will save time - even small issues such as like capitalisation).</p>"


def getExpressedTerm(p_name, term):
    if not term: return
    term = term.strip()
    if p_name == PROP_TARGET_READER:
        return q_what(term)[-1]
    elif p_name == PROP_TOPIC_NAME:
        exp_term = q_what(term)[-1]
        # return f"{exp_term[0].upper()}{exp_term[1:]}"
        return exp_term
    elif p_name == PROP_TOPIC_IMPACT:
        return q_what(term)[-1]
    elif p_name == PROP_TARGET_IMPRESSION:
        return term[2:] if term[0:1] == "to" else term
    # elif p_name == PROP_TOPIC_CAUSE:
    #     return term
    return term

ARTICLE_LIST = ["a", "an", "the"]

def getUnexpressedTerm(exp_term):
    exp_term = exp_term.strip()
    exp_term_words = [x for x in exp_term.split(" ") if x.strip()]
    return " ".join(exp_term_words[1:]) if exp_term_words[0] in ARTICLE_LIST else exp_term


# questions/subquestions stage

def getQuestionsDict(project):
    qdict = {}

    prop_target_reader = project.props.get(name=PROP_TARGET_READER)
    prop_topic_name = project.props.get(name=PROP_TOPIC_NAME)
    prop_target_impression = project.props.get(name=PROP_TARGET_IMPRESSION)
    prop_topic_impact = project.props.get(name=PROP_TOPIC_IMPACT)
    
    prop_target_reader_exp = prop_target_reader.response_exp
    prop_topic_name_response = prop_topic_name.response

    # placeholder values
    prop_target_reader_exp = "investors"
    prop_topic_name_response = "Nicola Tesla"

    qdict = {
        "0": {
            'has_subq': False,
            'q': f"Who is <span class='editable'>{prop_topic_name_response}</span>?",
            'ql': f"{prop_topic_name_response} is...",
        }, 
        "1": {
            'has_subq': False,
            'q': f"In what way will <span class='editable'>{prop_topic_name_response}</span> affect {prop_target_reader_exp}?",
            'ql': f"{prop_topic_name_response} will affect {prop_target_reader_exp} by...",
        }, 
        "2": {
            'has_subq': True,
            'subq': {
                "2_1": {
                    'sq': f"Why will <span class='editable'>{prop_topic_name_response}</span> benefit {prop_target_reader_exp}?",
                    'sql': f"{prop_topic_name_response} will benefit {prop_target_reader_exp} because...",
                    'nxt_sq_id': "2_2",
                },
                "2_2": {
                    'sq': f"When will <span class='editable'>{prop_topic_name_response}</span> benefit {prop_target_reader_exp}?",
                    'sql': f"{prop_topic_name_response} will benefit {prop_target_reader_exp} at...",
                    'prv_sq_id': "2_1",
                    'nxt_sq_id': "2_3",
                },
                "2_3": {
                    'sq': f"How will <span class='editable'>{prop_topic_name_response}</span> benefit {prop_target_reader_exp}?",
                    'sql': f"{prop_topic_name_response} will benefit {prop_target_reader_exp} by...",
                    'prv_sq_id': "2_2",
                },
            },
        }
    }

    return qdict

def getChoiceHeading_topics(project):
    proj_doc_subtype = PROJ_SUBTYPE_CHOICES_SEL_LIST[project.doc_type][project.doc_subtype].lower()
    prop_topic_name_response = project.props.get(name=PROP_TOPIC_NAME).response

    # placeholders
    # proj_doc_subtype = "report"
    prop_topic_name_response = "off-roading"
    choice_count = 3
    return f"What topics do you want to include in this {proj_doc_subtype} about <span class='editable'>{prop_topic_name_response}</span>?", f"Please choose {choice_count}", choice_count

def getTopicsChoiceList(project):
    prop_topic_name_response = project.props.get(name=PROP_TOPIC_NAME).response

    # placeholder
    chList = [
        "Elements of off-roading",
        "Types of off-roading",
        "Wikipedia of off-roading",
        "Mud tyres",
    ]

    return chList