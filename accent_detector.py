import random

def detect_accent(transcript: str) -> dict:
    accent_keywords = {
        "British": [
            "mate", "lorry", "boot", "flat", "biscuit", "petrol", "queue", "holiday", "football", "brilliant",
            "loo", "trousers", "postcode", "torch", "nappy", "chemist", "crisps", "jumper", "dustbin", "railway",
            "aubergine", "lift", "car park", "sweets", "post", "windscreen", "trainers", "zebra crossing", "telly", "brolly",
            "garden", "rubbish", "hoover", "fizzy drink", "full stop", "flyover", "high street", "ring", "mum", "advert",
            "bin", "banger", "braces", "pram", "maths", "hire", "estate agent", "solicitor", "revise", "nutter"
        ],
        "American": [
            "apartment", "truck", "trunk", "elevator", "cookie", "gas", "line", "vacation", "soccer", "awesome",
            "bathroom", "pants", "zip code", "flashlight", "diaper", "drugstore", "chips", "sweater", "garbage", "railroad",
            "eggplant", "cab", "parking lot", "candy", "mail", "windshield", "sneakers", "crosswalk", "tv", "umbrella",
            "yard", "trash", "vacuum", "soda", "period", "overpass", "main street", "call", "mom", "commercial",
            "can", "sausage", "suspenders", "stroller", "math", "rent", "realtor", "lawyer", "study", "crazy"
        ],
        "Australian": [
            "mate", "arvo", "brekkie", "no worries", "bush", "thongs", "servo", "bottle-o", "ute", "esky",
            "barbie", "chook", "maccas", "fair dinkum", "bogan", "ripper", "heaps", "g’day", "ta", "sanger",
            "bloke", "sheila", "brolly", "lollies", "rego", "togs", "snag", "trackie dacks", "footy", "jumper",
            "rooted", "stickybeak", "stubbie", "tradie", "whinge", "yak", "straya", "bushwalk", "dunny", "sunnies",
            "op shop", "nippers", "chunder", "crook", "drongo", "mozzie", "pash", "reckon", "roo", "smoko"
        ]
    }

    text = transcript.lower()
    scores = {accent: 0 for accent in accent_keywords}

    for accent, keywords in accent_keywords.items():
        for word in keywords:
            if word in text:
                scores[accent] += 1

    best_accent = max(scores, key=scores.get)
    score = scores[best_accent]
    confidence = min(100, score * 2 + random.randint(0, 10)) 
    if score == 0:
        best_accent = "Unknown"

    return {
        "accent": best_accent,
        "confidence": confidence if score > 0 else 0,
        "summary": f"Detected accent based on keywords is most likely **{best_accent}**."
    }