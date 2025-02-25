# WhatsppInvitationSender

# Invitation Card Generator

This project generates personalized invitation cards using a template image and recipient details from a CSV file. It also sends the invitation over WhatsApp.

## Features
- Reads recipient details (name, family status, and mobile number) from a CSV file.
- Generates personalized invitation cards with the recipient's name.
- Saves the customized invitation cards as images.
- Sends the generated invitation card via WhatsApp.

## Requirements
### Dependencies
Ensure you have the following Python libraries installed:
```sh
pip install pillow pywhatkit
```

### Required Files
- **Invitation Template.jpg**: The template image for the invitation.
- **Relatives.csv**: A CSV file containing recipient details.
- **Charmonman-Bold.ttf**: The font file used for writing text on the image.

## File Structure
```
|-- Invitation Template.jpg
|-- Relatives.csv
|-- Charmonman-Bold.ttf
|-- script.py (Main Python script)
|-- Invitation Cards/ (Generated invitation cards)
```

## CSV Format
The `Relatives.csv` file should have the following columns:
```csv
Name,Family,Mobile
John Doe,With Family,+12345678901
Jane Smith,Individual,+10987654321
```
- **Name**: Recipient's name
- **Family**: "With Family" if the recipient is invited with their family, otherwise any other value
- **Mobile**: Recipient's phone number in international format (e.g., +12345678901)

## How It Works
1. The script loads the invitation template.
2. It reads the recipient details from the CSV file.
3. It writes the recipient's name on the invitation card.
4. Saves the modified image in the `Invitation Cards/` directory.
5. Sends the generated card via WhatsApp (if the phone number is valid).

## WhatsApp Integration
- The script uses `pywhatkit.sendwhats_image()` to send invitations via WhatsApp.
- The phone number must be in international format.
- Ensure that WhatsApp Web is logged in before running the script.

## Running the Script
Execute the script using:
```sh
python script.py
```

## Notes
- The font file (`Charmonman-Bold.ttf`) must be in the same directory as the script.
- The script validates phone numbers before sending messages.
- Ensure the `Invitation Cards/` directory exists or will be created by the script.
- Adjust the text position and font size if needed.

## Output Sample
![img.png](img.png)

## License
This project is open-source and available for use under the MIT License.

## Image Attribution

The template image used in this project is sourced from outside. Image credit goes to the original creator.

