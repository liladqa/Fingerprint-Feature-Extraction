def determine_vector(term, bif):
    countTermLocX = 0
    countTermLocY = 0
    for index, feature in enumerate(term):
        countTermLocX += feature.locX
        countTermLocY += feature.locY

    countBifLocX = 0
    countBifLocY = 0
    for index, feature in enumerate(bif):
        countBifLocX += feature.locX
        countBifLocY += feature.locY

    try:
        termRatio = countTermLocX/countTermLocY
    except ZeroDivisionError:
        termRatio = 0

    try:
        bifRatio = countBifLocX/countBifLocY
    except ZeroDivisionError:
        bifRatio = 0

    try:
        xRatio = countTermLocX/countBifLocX
    except ZeroDivisionError:
        xRatio = 0

    try:
        yRatio = countTermLocY/countBifLocY
    except ZeroDivisionError:
        yRatio = 0

    return [countTermLocX, countTermLocY, countBifLocX, countBifLocY, termRatio, bifRatio, xRatio, yRatio]
