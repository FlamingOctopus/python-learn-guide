def create_new_string(string):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    key = 25
    list = []
    for sym in string:
        if sym.isupper():
            list.append(upper[(upper.find(sym) + key) % 26])
        elif sym == " ":
            list.append(' ')
        elif sym == '/':
            list.append('\n')
        else:
            list.append(lower[(lower.find(sym) + key) % 26])
    new_string = "".join(list)
    return new_string


def create_strings(string):
    strings = string.split()
    list_words = []
    string = ""
    for word in strings:
        if not '/' in word:
            string += word + " "
        else:
            string += word
            list_words.append(string)
            string = ""
    return list_words


def cesar_decode(list_words):
    decoded_strings = []
    shift = -3
    for item in list_words:
        decoded_strings.append(decode_string(item, shift))
        shift -= 1
    return decoded_strings


def decode_string(string, shift):
    separated_string = string.split()
    decoded_string = ""
    for word in separated_string:
        string = word[(len(word) + shift) % len(word):] + word[:(len(word) + shift) % len(word)]
        decoded_string += string + " "
    return decoded_string


string = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

mod_string = "".join(cesar_decode(create_strings(string)))
print(create_new_string(mod_string))
