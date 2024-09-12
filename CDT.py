__author__ = "santiago Nicoals revelo saavedra"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "santiago.revelo@campusucc.edu.co"

class CDT:
        
    '''#---------------------------------------
    # Aquí inicia la declaración del CDT
    ----------------------------------------#'''

    saldo = 0
    interes_mensual = 0
    meses_restantes = 0

    '''#---------------------------------------
    # # 1 = Activo, 2 = Inactivo
    ----------------------------------------#'''

    estado = 1
    
    __metodo__= "DarInteresMensual"
    __parameter__= "Ninguno "
    __retorno__= "interes mensual"
    __descripcion__="metodo que dara el interes de cada mes "
    
    def DarInteresMensual(self):
        return self.interes_mensual
    
    __metodo__= "ActualizarSaldoPorPasoMes"
    __parameter__= "Ninguno "
    __retorno__= "saldo"
    __descripcion__="metodo que actualizara el saldo cada mes "
    
    def ActualizarSaldoPorPasoMes (self):
        return self.saldo
    
    __metodo__= "DarSaldo"
    __parameter__= "Ninguno "
    __retorno__= "saldo de la cuenta"
    __descripcion__="metodo que retorne el saldo de la cuenta del cliente "
    
    def DarSaldo (self):
        return self.saldo