from pytube import YouTube
import pyfiglet

print(pyfiglet.figlet_format("YOUTUBE DOWNLOADER"))

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print('Erro no Download Tente novamente')
    

link = input("COLE SEU LINK AQUI: ")
Download(link) 
print('DOWNLOAD FEITO COM SUCESSO!!!') 

