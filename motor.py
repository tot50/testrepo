class Motor : 
    __tipo = None


    def __init__(self, tipo):
        self.__tipo = tipo
    def  getTipo(self):
        return self.__tipo

class Auto :
    __mmarca = None 
    __modelo = None
    __motor = None

    def __init__(self, marca, modelo, motor):
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = Motor


    def mostrarinfo(self):
        print("El auto es de la marca" + self.__marca + " con un modelo "+ self.__modelo + " motor tipo " + self.getmotor.getTipo())

def main():
    pass

if __name__ == "__main__":
    main ()