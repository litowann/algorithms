def find_image():
    image = input('Enter your image: ')

    p = [0] * len(image)

    j = 0
    i = 1

    while i < len(image):
        if image[j] == image[i]:
            p[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j - 1]

    text = input('Enter your text: ')

    m = len(image)
    n = len(text)

    i = 0
    j = 0

    while i < n:
        if text[i] == image[j]:
            i += 1
            j += 1

            if j == m:
                print("Your image in the text was found.")
                break
        elif j > 0:
            j = p[j - 1]
        else:
            i += 1
        if i == n:
            print('Your image was not found.')
            break
