
import cv2
import numpy as np
import random as rnd
from fuzzywuzzy import fuzz

countries = ['afghanistan.png', 'albania.png', 'algeria.png', 'american samoa.png', 'andorra.png', 'angola.png', 'antarctica.png', 'antigua and barbuda.png', 'argentina.png', 'armenia.png', 'aruba.png', 'australia.png', 'austria.png', 'azerbaijan.png', 'bahamas.png', 'bahrain.png', 'bangladesh.png', 'barbados.png', 'belarus.png', 'belgium.png', 'belize.png', 'benin.png', 'bermuda.png', 'bhutan.png', 'bolivia.png', 'bosnia.png', 'botswana.png', 'brazil.png', 'british indian ocean territory.png', 'british virgin islands.png', 'brunei.png', 'bulgaria.png', 'burkina faso.png', 'burundi.png', 'cambodia.png', 'cameroon.png', 'canada.png', 'cape verde.png', 'central african republic.png', 'chad.png', 'chile.png', 'china.png', 'christmas island.png', 'cocos (keeling) islands.png', 'colombia.png', 'comoros.png', 'congo.png', 'costa rica.png', 'croatia.png', 'cuba.png', 'cyprus.png', 'czech republic.png', 'denmark.png', 'djibouti.png', 'dominica.png', 'dominican republic.png', 'drc.png', 'ecuador.png', 'egypt.png', 'el salvador.png', 'england.png', 'equatorial guinea.png', 'eritrea.png', 'estonia.png', 'ethiopia.png', 'faroe islands.png', 'fiji.png', 'finland.png', 'france.png', 'french guiana.png', 'french polynesia.png', 'gabon.png', 'gambia.png', 'georgia.png', 'germany.png', 'ghana.png', 'gibraltar.png', 'greece.png', 'greenland.png', 'grenada.png', 'guam.png', 'guatemala.png', 'guernsey.png', 'guinea-bissau.png', 'guinea.png', 'guyana.png', 'haiti.png', 'honduras.png', 'hong kong.png', 'hungary.png', 'iceland.png', 'india.png', 'indonesia.png', 'iran.png', 'iraq.png', 'ireland.png', 'isle of man.png', 'israel.png', 'italy.png', 'ivory coast.png', 'jamaica.png', 'japan.png', 'jersey.png', 'jordan.png', 'kazakhstan.png', 'kenya.png', 'kiribati.png', 'kosovo.png', 'kuwait.png', 'kyrgyzstan.png', 'laos.png', 'latvia.png', 'lebanon.png', 'lesotho.png', 'liberia.png', 'libya.png', 'liechtenstein.png', 'lithuania.png', 'luxembourg.png', 'macao.png', 'macedonia.png', 'madagascar.png', 'malawi.png', 'malaysia.png', 'maldives.png', 'mali.png', 'malta.png', 'marshall islands.png', 'mauritania.png', 'mauritius.png', 'mayotte.png', 'mexico.png', 'micronesia.png', 'moldova.png', 'monaco.png', 'mongolia.png', 'montenegro.png', 'morocco.png', 'mozambique.png', 'myanmar.png', 'namibia.png', 'nauru.png', 'nepal.png', 'netherlands.png', 'new caledonia.png', 'new zealand.png', 'nicaragua.png', 'niger.png', 'nigeria.png', 'niue.png', 'norfolk island.png', 'north korea.png', 'northen irland.png', 'norway.png', 'oman.png', 'pakistan.png', 'palau.png', 'panama.png', 'papua new guinea.png', 'paraguay.png', 'peru.png', 'philippines.png', 'pitcairn.png', 'poland.png', 'portugal.png', 'puerto rico.png', 'qatar.png', 'romania.png', 'russia.png', 'rwanda.png', 'saint barthelemy.png', 'saint helena.png', 'saint kitts and nevis.png', 'saint lucia.png', 'saint vincent & the grenadines.png', 'samoa.png', 'san marino.png', 'sao tome and principe.png', 'saudi arabia.png', 'scotland.png', 'senegal.png', 'serbia.png', 'seychelles.png', 'sierra leone.png', 'singapore.png', 'slovakia.png', 'slovenia.png', 'solomon islands.png', 'somalia.png', 'south africa.png', 'south korea.png', 'south sudan.png', 'spain.png', 'sri lanka.png', 'sudan.png', 'suriname.png', 'swaziland.png', 'sweden.png', 'switzerland.png', 'syria.png', 'taiwan.png', 'tajikistan.png', 'tanzania.png', 'thailand.png', 'timor-leste.png', 'togo.png', 'tokelau.png', 'tonga.png', 'trinidad and tobago.png', 'tunisia.png', 'turkey.png', 'turkmenistan.png', 'tuvalu.png', 'uganda.png', 'ukraine.png', 'united arab emirates.png', 'united kingdom.png', 'united states.png', 'uruguay.png', 'us virgin islands.png', 'uzbekistan.png', 'vanuatu.png', 'vatican.png', 'venezuela.png', 'vietnam.png', 'wales.png', 'yemen.png', 'zambia.png', 'zimbabwe.png']
def find_most_similar_string(target_string, string_list):
    most_similar_string = max(string_list, key=lambda x: fuzz.ratio(target_string, x))
    return most_similar_string

def resize_image(image, target_size):
    # Resize the image to the target size
    return cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

def calculate_similarity_percentage(image1, image2, tolerance=50):
    # Calculate the absolute difference between the two images
    diff = cv2.absdiff(image1, image2)

    # Create a binary mask where differences are below the tolerance
    mask = np.all(diff < tolerance, axis=-1)

    # Calculate the percentage of similar pixels
    similarity_percentage = (np.sum(mask) / mask.size) * 100

    return similarity_percentage

def visualize_similarity(image1, image2, tolerance=50):
    # Calculate the absolute difference between the two images
    diff = cv2.absdiff(image1, image2)

    # Create a binary mask where differences are below the tolerance
    mask = np.all(diff < tolerance, axis=-1)

    # Create a copy of the original image
    result_image = image1.copy()

    # Set a specific color (black) for non-similar pixels
    result_image[~mask] = [0, 0, 0]

    return result_image

def main():
    correct_country = rnd.choice(countries)
    count = 0
    while True:
        count+=1
        image1_path = "flags/" + correct_country
        guessed_country = input("Guess a country flag (type 'exit' to stop): ").strip()

        if guessed_country.lower().strip() == 'exit':
            print(correct_country)
            break
        guessed_country = find_most_similar_string(guessed_country,countries) 
        print("you guessed: "+ guessed_country)
        image2_path = "flags/" + guessed_country

        # Load images
        img1 = cv2.imread(image1_path)
        img2 = cv2.imread(image2_path)

        # Check if images have the same dimensions
        if img1.shape != img2.shape:
            # Resize images to a common size (you can adjust the target_size)
            target_size = (int(min(img1.shape[1], img2.shape[1]) / 2), int((img1.shape[0] + img2.shape[0]) / 4))
            img1 = resize_image(img1, target_size)
            img2 = resize_image(img2, target_size)

        # Visualize the similarity
        result_image = visualize_similarity(img1, img2)
        similarity_percentage = calculate_similarity_percentage(img1, img2)

        # Display similarity percentage
        print(f"Similarity Percentage: {similarity_percentage:.2f}%")

        # Display the result image
        correct_flag_resized = resize_image(result_image, (int(result_image.shape[1] * 0.5), int(result_image.shape[0] * 0.5)))
        cv2.imshow("Similarity Visualization", correct_flag_resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if guessed_country.lower() == correct_country.lower():
            print("Congratulations! You guessed correctly. It took you "+str(count)+" tries.")
            break
        else:
            print("Incorrect guess. Try again.")
main()