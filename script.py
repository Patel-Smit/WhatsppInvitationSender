# MIT License
# Copyright (c) 2025 Smit Patel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction...

from PIL import Image, ImageDraw, ImageFont
import csv
import os
import pywhatkit
import re

FONT_PATH = "Charmonman-Bold.ttf"
IMAGE_PATH = "Invitation Template.jpg"
CSV_PATH = "Relatives.csv"
OUTPUT_DIR = "./Invitation Cards/"
TEXT_COLOR = (231, 12, 129, 1)
TEXT_POSITION = (311, 915)
FONT_SIZE = 45

# Load the original image
original_image = Image.open(IMAGE_PATH)

# Define the text properties
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
except IOError:
    print(f"Font file not found. Ensure '{FONT_PATH}' is in the script directory.")
    exit()

TEXT_COLOR = (231, 12, 129, 1)

# Ensure the directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read the CSV file using DictReader
with open(CSV_PATH, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Name", "Family", "Mobile"])
    next(reader, None)  # Skip the header row

    for row in reader:
        text = row["Name"].strip()
        family_status = row.get("Family", "").strip().lower()
        family = '𝙮𝙤𝙪 𝙬𝙞𝙩𝙝 𝙮𝙤𝙪𝙧 𝙛𝙖𝙢𝙞𝙡𝙮' if "with family" in family_status else '𝘺𝘰𝘶'

        full_text = f"{text}"

        # Create a fresh copy of the original image for each iteration
        image = original_image.copy()
        draw = ImageDraw.Draw(image)

        # Calculate the position to center the text
        text_length = draw.textlength(full_text, font)

        # Add text to the image
        draw.text(TEXT_POSITION, full_text, fill=TEXT_COLOR, font=font)

        # Save the modified image
        output_path = os.path.join(OUTPUT_DIR, f"{text}.jpg")
        image.save(output_path)
        #  image.show() -> if you want to get the preview of the image

        # Sends Invitation over Whatsapp
        def is_valid_phone_number(phone):
            return re.match(r"^\+\d{11,15}$", phone) is not None  # Matches international numbers

        phone_number = row["Mobile"].replace(" ", "")
        message = f'''
            ✨ 𝐂𝐞𝐥𝐞𝐛𝐫𝐚𝐭𝐢𝐨𝐧 ✨\n\n𝘞𝘦 𝘫𝘰𝘺𝘰𝘶𝘴𝘭𝘺 𝘪𝘯𝘷𝘪𝘵𝘦 {family} 𝘵𝘰 𝘤𝘦𝘭𝘦𝘣𝘳𝘢𝘵𝘦 𝘵𝘩𝘦 ....\n\n🌸 𝗗𝗮𝘁𝗲: 00/00/0000 \n⏰ 𝗧𝗶𝗺𝗲: 00 AM \n🍽 𝗟𝘂𝗻𝗰𝗵: 00 AM\n\n📍 𝗩𝗲𝗻𝘂𝗲: ABC Street, XYZ, Qwertyuiop\n\nhttps://maps.google.com\n\n𝘓𝘦𝘵 𝘶𝘴 𝘤𝘰𝘮𝘦 𝘵𝘰𝘨𝘦𝘵𝘩𝘦𝘳 𝘵𝘰 𝘤𝘳𝘦𝘢𝘵𝘦 𝘯𝘦𝘸 𝘮𝘦𝘮𝘰𝘳𝘪𝘦𝘴 𝘵𝘰 𝘵𝘳𝘦𝘢𝘴𝘶𝘳𝘦.\n\n𝗪𝗶𝘁𝗵 𝗟𝗼𝘃𝗲 𝗮𝗻𝗱 𝗚𝗿𝗮𝘁𝗶𝘁𝘂𝗱𝗲, *PATEL FAMILY*💖
            '''
        if is_valid_phone_number(phone_number):
            pywhatkit.sendwhats_image(phone_number, output_path, caption=message, tab_close=True)
        else:
            print(f"Skipping invalid phone number: {phone_number}")

        # Print for debugging
        print(full_text, "saved at", output_path, family)

