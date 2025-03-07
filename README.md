

ENGLISH (SCROLL DOWN FOR DUTCH)

### General Info  

**Application Name:** RTS-App  

**Goal:**  
The aim is to create an app that can compete with BigCartel, specifically targeting bands for selling merchandise (both online and at live shows, with the current priority being live shows).  

**Key Features:**  

### **Article Number Generator:**  
This app should automatically generate a logical article number when entering new items.  
The number will consist of values linked to stock tables, including:  

- **Release Year**  
- **Type** (e.g., CD, Vinyl, Shirt – each type gets a unique value)  
- **Design** (e.g., which CD – each design gets a unique value)  
- **Size** (each size gets a unique value)  
- **Limited Edition** (Yes or No also gets a unique value)  

**Generation Order:**  
1. **Release Year:** Takes the year of entry and uses the last two digits (e.g., 2025 → 25).  
2. **Type Number:** Comes from the "producttype" table and uses the ID.  
3. **Design Number:** Comes from the "designs" table and uses the Primary Key.  
4. **Size Number:** Comes from the "sizes" table and uses the Primary Key.  
5. **Limited Edition Number:** Comes from the "limited_edition" table and uses the Primary Key.  

These values are then combined in this order to ensure each item gets a unique number. Each size of the same clothing item also gets a unique article number.  

### **Inventory Management:**  
- Easily and quickly view the stock of all merchandise.  
- Quickly see the sales history per item, as well as where each item was sold.  
- Smooth entry of new products and seamless generation of article numbers.  

### **Nice-to-Have Features:**  
- Option to print address labels (for online sales).  
- Potential future expansion into warehouse management software.  
- Integration with PayConiq (or another payment platform).  

### **Technical Details:**  
- **Database:** PostgreSQL (Supabase)  
- **Backend:** Python 3.12.6 (Django)  
- **Frontend:** Django  

**Not yet implemented:**  
- QR Code: `pip install qrcode[pil]`  
- Barcode: `pip install python-barcode`  

### **Notes & Tips:**  
- **Mollie (payment):** Still under consideration, as there is currently no free version.  


=========================================================================================================================================================================================================================================================

# Algemene info  

## Naam applicatie: RTS-App  

## Doel  
Het is de bedoeling om een app te maken die kan concurreren met BigCartel,  
dus specifiek op bands gericht om goederen te verkopen  
(zowel online als op optredens, prioriteit momenteel is op optredens).  

## Troeven  

### **Artikelnummer generator**  
Het is de bedoeling om in deze app automatisch een logisch artikelnummer te laten genereren bij het invoeren van nieuwe artikelen.  
Dit nummer zal bestaan uit alle waardes die gelinkt zijn aan de tabellen van de stock:  

- **Release jaar**  
- **Type** (bijv. CD, Vinyl, Shirt; elk type krijgt een unieke waarde)  
- **Design** (bijv. welke cd; elk design krijgt een unieke waarde)  
- **Maat** (elke maat krijgt een unieke waarde)  
- **Limited Edition** (Ja of Nee krijgt telkens een waarde)  

**De volgorde van genereren:**  

1. **Releasejaar:** neemt de datum van invoer en gebruikt de laatste 2 cijfers (bijv. 2025 → 25).  
2. **Typenummer:** komt uit de tabel `"producttype"` en neemt de ID.  
3. **Designnummer:** komt uit de tabel `"designs"` en neemt de Primary Key uit de tabel.  
4. **Maatnummer:** komt uit de tabel `"sizes"` en neemt de Primary Key uit de tabel.  
5. **Limited Edition-nummer:** komt uit de tabel `"limited_edition"` en neemt de Primary Key uit de tabel.  

Deze waarden worden dan in deze volgorde samengevoegd, zodat elk artikel een uniek nummer krijgt.  
Elke maat van hetzelfde kledingstuk krijgt ook een uniek artikelnummer.  

### **Voorraadbeheer**  
- Makkelijk en snel de voorraad kunnen bekijken van alle merchandise.  
- Snel de verkoopgeschiedenis per artikel kunnen zien, evenals waar het verkocht is.  
- Vlotte invoer van nieuwe producten en automatische generatie van artikelnummers.  

## Nice to have's  
- Eventueel adreslabel printen (bij online verkoop).  
- Op termijn uitbreiden naar magazijnsoftware.  
- Integratie van PayConiq (of ander betaalplatform).  

## Technische details  
- **Database:** PostgreSQL (Supabase)  
- **Backend:** Python 3.12.6 (Django)  
- **Frontend:** Django  

### **Nog niet geïmplementeerd:**  
- **QR-code:** `pip install qrcode[pil]`  
- **Barcode:** `pip install python-barcode`  

## Opmerkingen en tips  
- **Mollie (betaling):** Nog te bekijken, voorlopig geen gratis versie.  
