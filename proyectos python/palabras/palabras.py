organización = "Gonzalo" 

print("Aprende a programar con " + organización)  
print("Aprende a programar con {}".format(organización))  
print(f"Aprende a programar con {organización}") # f-string
 
# Mad Libs (Historia Locas) 
 
adj = input("Adjetivo: ")  
verbo1 = input("Verbo: ")
verbo2 = input("verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")  

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} y alcanza tus {sustantivo_plural}!"
 
print(madlib) 