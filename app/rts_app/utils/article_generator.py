from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def generate_article_number(producttype, design, size=None, limited_edition=None):
    """
    Genereert een uniek artikelnummer op basis van:
    - Releasejaar (laatste 2 cijfers)
    - ProductType (2 cijfers)
    - Design (2 cijfers)
    - Size (2 cijfers, 99 als geen kleding)
    - Limited Edition (2 cijfers, altijd 01 of 02)
    """

    
    year = datetime.now().year % 100 
    typenr = f"{producttype.typenr:02}" if producttype else "00"
    designnr = f"{design.designnr:02}" if design else "00"
    if producttype and not producttype.clothing:
        sizenr = "99"
    else:
        sizenr = f"{size.sizenr:02}" if size else "00"

    lenr = f"{limited_edition.lenr:02}" if limited_edition else "02"

    article_number = f"{year}{typenr}{designnr}{sizenr}{lenr}"
    return int(article_number)

    logger.debug("Generating article number with: Year: %s, Type: %s, Design: %s, Size: %s, Limited Edition: %s", year, typenr, designnr, sizenr, lenr)
    return int(article_number)