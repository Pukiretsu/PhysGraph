import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
import math as mt

#Cargamos los iconos e imagenes
image = open('Scientist.gif', 'rb')
b64 = image.read()

icon = open('icono.ico', 'rb')
b64ico = icon.read()

# Configuracion del tema
sg.theme('Light Blue')

# Llama al layout de todo lo relacionado al MUA
MLyout = [  
            [sg.Button(key='-MUAxd-', button_text='Movimiento', pad=((5,10),(5,0)), button_color=('Teal',sg.theme_background_color())),
             sg.Button(key='-Tray-', button_text='Trayectoria', pad=((5,0),(5,0)), button_color=('Grey',sg.theme_background_color()))],

            [sg.Text("___________________________________________________________________", text_color='Teal', pad=(0,(0,30)))],
            
            [
             sg.Button(key='-PosB-',  button_text = 'Posicion'   , pad = ((20,110),(5,0))), 
             sg.Text('Velocidad Inicial'     , key='-V0t-' , pad = ((0,0),(10,3)) ), 
             sg.Text('Aceleración'           , key='-At-'  , pad = (40,   (10,3)) ), 
             sg.Text('Posición Inicial'      , key='-X0t-' , pad = ((0,0),(10,3)) )
            ],

            [
             sg.Button(key='-VelB-',  button_text = 'Velocidad'  , pad = ((20,111),(5,0))), 
             sg.Input(key='-V0-',default_text='0',  size=(6,0) , background_color=('light blue'), disabled=True), sg.Button(' ', key='-V0c-', pad=((5,45),(0,0))), 
             sg.Input(key='-A-' ,default_text='0',  size=(6,0) , background_color=('light blue'), disabled=True), sg.Button(' ', key='-Ac-' , pad=((5,45),(0,0))), 
             sg.Input(key='-X0-',default_text='0',  size=(6,0) , background_color=('light blue'), disabled=True), sg.Button(' ', key='-X0c-', pad=((5,0),(0,0)) )
            ],

            [
             sg.Button(key='-TimeB-', button_text = 'Tiempo', pad = ((20,117),(5,0))), 
             sg.Text('Velocidad Final'      , key='-V1t-' , pad = ((0,0),(10,3))  ), 
             sg.Text('Tiempo'               , key='-Tt-'  , pad = ((55,59),(0,0)) ), 
             sg.Text('Posición Final'       , key='-X1t-' , pad = ((0,0),(10,3))  ),
            ],
            
            [
             sg.Button(key='-AcelB-', button_text = 'Aceleracion', pad = ((20,100),(5,0))), 
             sg.Input(key='-V1-',default_text='0',  size=(6,0) , background_color=('light blue'), disabled=True), sg.Button(' ', key='-V1c-', pad=((5,45),(0,0))), 
             sg.Input(key='-T-' ,default_text='0',  size=(6,0) , background_color=('light blue'), disabled=True), sg.Button(' ', key='-Tc-' , pad=((5,45),(0,0))), 
             sg.Input(key='-X1-',default_text='0',  size=(6,0) , background_color=('light blue'), disabled=True), sg.Button(' ', key='-X1c-', pad=((5,0),(0,0)) )
            ],
            
            [sg.Button('Calcular', pad=((400,0),(20,0)), key='-Calculate-', disabled=True, disabled_button_color=('Light Grey',sg.theme_background_color())),
            #  sg.Button('Guardar',  pad=((0,0),  (20,0)), key='-Save-',      disabled=True, disabled_button_color=('Light Grey',sg.theme_background_color())),
             sg.Button('Volver',   pad=((30,10), (20,0)), key='-Back-')]
         ]

# Llama al layout de todo lo relacionado con Trayectorias
TLyout = [  
            [sg.Button(key='-MUA-', button_text='Movimiento', pad=((5,10),(5,0)), button_color=('Grey',sg.theme_background_color())),
             sg.Button(key='-Trayxd-', button_text='Trayectoria', pad=((5,0),(5,0)), button_color=('Teal',sg.theme_background_color()))], 
            
            [sg.Text("___________________________________________________________________", text_color='Teal', pad=((0,0),(0,10)))],

            [sg.Text("Altura inicial (m)",  pad=(120,1)), 
             sg.Text("Angulo de Tiro (°)",  pad=(15,1))],

            [sg.Input("0",      key='-y0-',     size=(6,0), pad=((145,0),(10,10)), background_color=('light blue') ),
             sg.Input("0",      key='-alpha-',  size=(6,0), pad=((200,0),(10,10)), background_color=('light blue') )],
            
            [sg.Text("Gravedad (m/s2)"   ,  pad=(115,1)), 
             sg.Text("Velocidad Inicial (m/s)")],

            [sg.Input("9.81",   key='-g-',      size=(6,0), pad=((145,0),(10,10)), background_color=('light blue') ),
             sg.Input("0",      key='-T_v0-',   size=(6,0), pad=((200,0),(10,10)), background_color=('light blue') )],
            
            [sg.Text(text='Alcance: '+str(0)+' m\nTiempo vuelo: '+str(0)+' s\n\nAltura maxima: '+str(0)+' m\nAltura maxima en X: '+str(0)+' m\nTiempo Y maximo: ' + str(0) + ' s', key= '-Result-', pad=((100,10),(10,10)),size=(35,6)),
             sg.Button(' ', image_data=b64)],

            [sg.Button('Calcular', pad=((400,0),(20,0)), key='-TCalculate-', disabled_button_color=('Light Grey',sg.theme_background_color())),
            sg.Button('Volver',   pad=((30,10), (20,0)), key='-TBack-')]
         ]

fLyout = [ 
            [sg.Text('PhysGraph',key='-Title-', text_color='Teal', font="BahnschriftLight 25", pad=((5,500),(5,250))),],
            
            [sg.Button(key='-New-', button_text='Nuevo', pad=((0,0),(0,0)))],

            [sg.Button(key='-About-', button_text='Acerca de', pad=((0,0),(5,0)))],

            # [sg.Input(key='-FILE-', visible=False, enable_events=True),
            #  sg.FileBrowse(key='-FileBrowse-', button_text='Abrir archivo', pad=((0,0),(0,20)), file_types=(('Hoja de Excel','*.xlsx*'),), enable_events=True)],
            
            [sg.Button(key='-Exit-',button_text='Salir', pad=((0,0),(20,0)))]
         ]

layout = [  
            [sg.Column(key='-FirstWindow-',layout=fLyout, pad=(5,0), visible=True,element_justification='right'),
             
            #Segunda ventana
             sg.Column(key='-MUAlayout-',layout=MLyout, visible=False, pad=(5,0)),
             sg.Column(key='-Tlayout-',layout=TLyout, visible=False, pad=(5,0))],
            
            [sg.Text('ver. 1.0', key='-Version-', text_color='Gray', font="BahnschriftLight 10")]
            
            ]

window = sg.Window  (   
                        title = 'PhysGraph Ver. 1.0', 
                        layout = layout,
                        icon = 'icono.ico',
                        grab_anywhere = True,
                        border_depth=0,
                        auto_size_buttons=True,
                        element_justification = "right", 
                        font = "BahnschriftLight", 
                        button_color = ('gray',sg.theme_background_color()),
                    )

# ------------------------- [Element Handling] ------------------------------- #

# Manejo Column element 

def Window_1Hide():
    window['-FirstWindow-']     .update (visible = False)

def Window_1Show():
    window['-FirstWindow-']     .update (visible = True)

def window_2Hide():
    window['-MUAlayout-'].update (visible = False)
    window['-Tlayout-'].update (visible = False)

def Window_MUAShow():
    window['-Tlayout-']         .update (visible = False)
    window['-MUAlayout-']       .update (visible = True)

def Window_TrayShow():
    window['-MUAlayout-']       .update (visible = False)
    window['-Tlayout-']         .update (visible = True)

# Activacion individual inputs 

def MUA_V0_Enable  (cf): 
    if cf == 1:
        window['-V0-']              .update (disabled = False, text_color = 'Black')
        window['-V0t-']             .update (text_color='Black')
        window['-V0c-']             .update (text = 'S', disabled = False, button_color=('Teal',sg.theme_background_color()))
    if cf == 2:
        window['-V0-']              .update (disabled = False, text_color = 'Black')
        window['-V0t-']             .update (text_color='Black')
        
def MUA_A_Enable   (cf): 
    if cf == 1:
        window['-A-']               .update (disabled = False, text_color = 'Black')
        window['-At-']              .update (text_color='Black')
        window['-Ac-']              .update (text = 'S', disabled = False, button_color=('Teal',sg.theme_background_color()))
    if cf == 2:
        window['-A-']               .update (disabled = False, text_color = 'Black')
        window['-At-']              .update (text_color='Black')
        
def MUA_X0_Enable  (cf): 
    if cf == 1:
        window['-X0-']              .update (disabled = False, text_color = 'Black')
        window['-X0t-']             .update (text_color='Black')
        window['-X0c-']             .update (text = 'S', disabled = False, button_color=('Teal',sg.theme_background_color()))
    if cf == 2:
        window['-X0-']              .update (disabled = False, text_color = 'Black')
        window['-X0t-']             .update (text_color='Black')
        
def MUA_V1_Enable  (cf): 
    if cf == 1:
        window['-V1-']              .update (disabled = False, text_color = 'Black')
        window['-V1t-']             .update (text_color='Black')
        window['-V1c-']             .update (text = 'S', disabled = False, button_color=('Teal',sg.theme_background_color()))
    if cf == 2:
        window['-V1-']              .update (disabled = False, text_color = 'Black')
        window['-V1t-']             .update (text_color='Black')
        
def MUA_T_Enable   (cf): 
    if cf == 1:
        window['-T-']               .update (disabled = False, text_color = 'Black')
        window['-Tt-']              .update (text_color='Black')
        window['-Tc-']              .update (text = 'S', disabled = False, button_color=('Teal',sg.theme_background_color()))
    if cf == 2:
        window['-T-']               .update (disabled = False, text_color = 'Black')
        window['-Tt-']              .update (text_color='Black')
        
def MUA_X1_Enable  (cf): 
    if cf == 1:
        window['-X1-']              .update (disabled = False, text_color = 'Black')
        window['-X1t-']             .update (text_color='Black')
        window['-X1c-']             .update (text = 'S', disabled = False, button_color=('Teal',sg.theme_background_color()))
    if cf == 2:
        window['-X1-']              .update (disabled = False, text_color = 'Black')
        window['-X1t-']             .update (text_color='Black')

# Desactivacion individual inputs

def MUA_V0_Disable (cf): 
    if cf == 1:
        window['-V0-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-V0t-']             .update (text_color='Grey')
        window['-V0c-']             .update (text = 'N', button_color=('Gray',sg.theme_background_color()))
    if cf == 2:
        window['-V0-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-V0t-']             .update (text_color='Grey')
        window['-V0c-']             .update (text = ' ', disabled = True )

def MUA_A_Disable  (cf): 
    if cf == 1:
        window['-A-']               .update (value='0', disabled = True, text_color = 'Grey')
        window['-At-']              .update (text_color='Grey')
        window['-Ac-']              .update (text = 'N', button_color=('Gray',sg.theme_background_color()))
    if cf == 2:
        window['-A-']               .update (value='0', disabled = True, text_color = 'Grey')
        window['-At-']              .update (text_color='Grey')
        window['-Ac-']              .update (text = ' ', disabled = True )

def MUA_X0_Disable (cf): 
    if cf == 1:
        window['-X0-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-X0t-']             .update (text_color='Grey')
        window['-X0c-']             .update (text = 'N', button_color=('Gray',sg.theme_background_color()))
    if cf == 2:
        window['-X0-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-X0t-']             .update (text_color='Grey')
        window['-X0c-']             .update (text = ' ', disabled = True )

def MUA_V1_Disable (cf): 
    if cf == 1:
        window['-V1-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-V1t-']             .update (text_color='Grey')
        window['-V1c-']             .update (text = 'N', button_color=('Gray',sg.theme_background_color()))
    if cf == 2:
        window['-V1-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-V1t-']             .update (text_color='Grey')
        window['-V1c-']             .update (text = ' ', disabled = True )

def MUA_T_Disable  (cf): 
    if cf == 1:
        window['-T-']               .update (value='0', disabled = True, text_color = 'Grey')
        window['-Tt-']              .update (text_color='Grey')
        window['-Tc-']              .update (text = 'N', button_color=('Gray',sg.theme_background_color()))
    if cf == 2:
        window['-T-']               .update (value='0', disabled = True, text_color = 'Grey')
        window['-Tt-']              .update (text_color='Grey')
        window['-Tc-']              .update (text = ' ', disabled = True )

def MUA_X1_Disable (cf): 
    if cf == 1:
        window['-X1-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-X1t-']             .update (text_color='Grey')
        window['-X1c-']             .update (text = 'N', button_color=('Gray',sg.theme_background_color()))
    if cf == 2:
        window['-X1-']              .update (value='0', disabled = True, text_color = 'Grey')
        window['-X1t-']             .update (text_color='Grey')
        window['-X1c-']             .update (text = ' ', disabled = True )

# Funciones que involucran las funciones de arriba

def MUA_Button_Reestablish(): # Reestablece las condiciones originales de los botones
    window['-PosB-' ]           .update (button_color = ('Grey',sg.theme_background_color()))
    window['-VelB-' ]           .update (button_color = ('Grey',sg.theme_background_color()))
    window['-TimeB-']           .update (button_color = ('Grey',sg.theme_background_color()))
    window['-AcelB-']           .update (button_color = ('Grey',sg.theme_background_color()))

def MUA_Input_Enable(): # Habilita todos los botones del layout MUA
    MUA_V0_Enable(2)
    MUA_A_Enable(2)
    MUA_X0_Enable(2)
    MUA_V1_Enable(2)
    MUA_T_Enable(2)
    MUA_X1_Enable(2)

def MUA_Input_Disable(): # Deshabilita todos los botones del layout MUA
    MUA_V0_Disable(2)
    MUA_A_Disable(2)
    MUA_X0_Disable(2)
    MUA_V1_Disable(2)
    MUA_T_Disable(2)
    MUA_X1_Disable(2)

def MUA_refresh(): # Refresca el Layout MUA Desactivando todo
    MUA_Input_Disable()
    MUA_Button_Reestablish()

# Funciones por Tipo de calculo

def MUA_Position():
    # Reactivacion inputs
    MUA_Input_Enable()
    MUA_A_Enable    (1) # Activacion especial con check

    # Se desactivan los inputs innecesarios :D
    MUA_X1_Disable  (2)
    MUA_V0_Disable  (2)
    
    # Habilita boton calculo
    window['-Calculate-']       .update (disabled = False)
    window['-PosB-']            .update (button_color = ('Teal',sg.theme_background_color()))

def MUA_Velocity():
    #Reactivacion inputs
    MUA_Input_Enable( )  
    MUA_V0_Enable   (1) # Activacion especial con check
    MUA_T_Enable    (1) # Activacion especial con check
    
    #Se desactivan los inputs innecesarios :D
    MUA_V1_Disable  (2)
    MUA_X0_Disable  (2)
    MUA_X1_Disable  (2)

    # Habilita boton calculo
    window['-Calculate-']       .update (disabled = False)
    window['-VelB-']            .update (button_color = ('Teal',sg.theme_background_color()))

def MUA_Time():
    #Reactivacion inputs
    MUA_Input_Enable( )
    MUA_V1_Enable   (1) # Activacion especial con check

    #Se desactivan los inputs innecesarios :D
    MUA_T_Disable   (2)
    MUA_V0_Disable  (2)

    # Habilita boton calculo
    window['-Calculate-']       .update (disabled = False)
    window['-TimeB-']           .update (button_color = ('Teal',sg.theme_background_color()))

def MUA_Aceleration():
    #Reactivacion inputs
    MUA_Input_Enable( )
    MUA_V0_Enable   (1) # Activacion especial con check
    
    #Se desactivan los inputs innecesarios :D
    MUA_A_Disable   (2)
    MUA_V1_Disable  (2)

    # Habilita boton calculo
    window['-Calculate-']       .update (disabled = False)
    window['-AcelB-']           .update (button_color = ('Teal',sg.theme_background_color()))

# -------------------------- [Funciones de Calculos] ------------------------------- #

def Calc(CType, config):
    
    iVL =       {
                 'V0' : int(values['-V0-']),
                 'V1' : int(values['-V1-']),
                 'T'  : int(values['-T-'] ),
                 'A'  : int(values['-A-'] ),
                 'X0' : int(values['-X0-']),
                 'X1' : int(values['-X1-'])
                }

    if CType == 1: # Posicion
        
        if config == 1: # Caso normal
            print ('Posicion Caso 1')
            return iVL['X0'] + iVL['V1'] + (iVL['A']*(iVL['T']**2)/2)
        
        elif config == 2: # No se tiene Aceleracion
            print ('Posicion Caso 2')
            return iVL['X0'] + ((iVL['V0'] + iVL['V1'])/2) * iVL['T']
    
    elif CType == 2: # Velocidad

        if config == 1: # Caso normalna
            print ('Velocidad Caso 1')
            return iVL['V0'] + (iVL['A']*iVL['T'])

        elif config == 2: # Calculo de velocidad inicial
            print ('Velocidad Caso 2')
            try:
                v0 = (iVL['X1'] - iVL['X0'] - (iVL['A']*(iVL['T']**2)/2)) / iVL['T']
                return v0 + (iVL['A']*iVL['T'])
            except ZeroDivisionError:
                return 'VNV-2'
            

        elif config == 3:
            print ('Velocidad Caso 3') # No tiene en cuenta el tiempo
            return mt.sqrt((iVL['V0']**2) + (2*iVL['A'] * (iVL['X1']-iVL['X0'])))
    
    elif CType == 3: # Tiempo

        if config == 1: # Se usa velocidad inicial
            print ('Tiempo Caso 1')
            try:
                t1 = (-iVL['V1'] + mt.sqrt((iVL['V1']**2) - (2*iVL['A']*(iVL['X1']-iVL['X0']))))/iVL['A']
                t2 = (-iVL['V1'] - mt.sqrt((iVL['V1']**2) - (2*iVL['A']*(iVL['X1']-iVL['X0']))))/iVL['A']
            except ZeroDivisionError:
                return 'VNV-2' # Manejo de errores division por cero
            
        elif config == 2: # se usa velocidad final
            print ('Tiempo Caso 2')
            try:
                t1 = (-iVL['V0'] + mt.sqrt((iVL['V0']**2) - (2*iVL['A']*(iVL['X1']-iVL['X0']))))/ iVL['A']
                t2 = (-iVL['V0'] - mt.sqrt((iVL['V0']**2) - (2*iVL['A']*(iVL['X1']-iVL['X0']))))/ iVL['A']
            except ZeroDivisionError:
                return 'VNV-2'
            
        if t1 > t2 and t1 > 0:
            return t1
        elif t2 > t1 and t2 > 0:
            return t2
        else:
            return 'VNV-1'
    
    elif CType == 4: # Aceleracion
        
        if config == 1: # Se usa la velocidad Inicial
            print ('Aceleracion Caso 1')
            try:
                return (2*(iVL['X1']-iVL['X0']-(iVL['V0']*iVL['T']))) / (iVL['T']**2)
            except ZeroDivisionError:
                return 'VNV-2'
            
        if config == 2:
            print ('Aceleracion Caso 2')
            try:
                return (2*(iVL['X1']-iVL['X0']-(iVL['V1']*iVL['T']))) / (iVL['T']**2)
            except ZeroDivisionError:
                return 'VNV-2'

def tCalc():
    t_iVL =     {
                    'y0'    :   float(values['-y0-']),
                    'alp'   :   mt.radians(float(values['-alpha-'])),
                    'g'     :   float(values['-g-']),
                    'v0'    :   float(values['-T_v0-'])
                }
    
    #   Operaciones generales de informacion   
    tvuelo = (  (-t_iVL['v0']*np.sin(t_iVL['alp'])) - mt.sqrt( ((t_iVL['v0']*np.sin(t_iVL['alp']))**2) + (2*t_iVL['g']*t_iVL['y0']) )  ) / -t_iVL['g']
    tvuelo =    round(tvuelo,2)
    
    d_max = t_iVL['v0']*np.cos(t_iVL['alp'])*tvuelo
    d_max =    round(d_max,2)

    t_ymax  =   ( t_iVL['v0']*mt.sin(t_iVL['alp']) ) / t_iVL['g']
    t_ymax  =   round(t_ymax,2)    
    ymax    =   t_iVL['y0'] + t_iVL['v0']*mt.sin(t_iVL['alp'])*t_ymax - ((t_iVL['g']*t_ymax**2)/2)
    ymax    =   round(ymax,2)    
    d_ymax  =   ( t_iVL['v0']*mt.cos(t_iVL['alp'])*t_ymax )
    d_ymax  =   round(d_ymax,2)
    
    # Solo descomentar para hacer Debugging
    # print (f"Tiempo de vuelo: {tvuelo} \t Distancia Maxima: {d_max}")
    # print (f"Tiempo para alcanzar la altura maxima: {t_ymax} \t Distancia al alcanzar la altura maxima: {d_ymax} \t Altura maxima {ymax}")

    #   Variables a plotear
    x = np.linspace(0, d_max)
    tray = t_iVL['y0'] + np.tan(t_iVL['alp'])*x - ( (t_iVL['g'] * x**2) /  (2 * ( t_iVL['g'] * np.cos(t_iVL['alp']) ) ** 2) )
    
    #   Configuraciones del plot
    ax = plt.subplot()
    ax.plot(x, tray)
    
    ax.set_ylim (bottom=0.)
    ax.set_xlim (left=0.)
    ax.set      (
                    xlabel ='Alcance (m)',
                    ylabel ='Altura (m)', 
                    title='Trayectoria'
                )
    ax.grid     (True)

    TextRes = 'Alcance: '+str(d_max)+' m\nTiempo vuelo: '+str(tvuelo)+' s\n\nAltura maxima: '+str(ymax)+' m\nAltura maxima en X: '+str(d_ymax)+' m\nTiempo Y maximo: '+str(t_ymax)+' s'
    window['-Result-'].update(value=TextRes)
    
    plt.show()

# ----------------------------- [Event and value Handling] -------------------------------

while True:
    event, values = window.read()
    
    # Descomentar si se va a hacer debugging
    # print(event, values)

    if event == '-New-':
        Window_1Hide()
        Window_MUAShow()
        MUA_refresh()

    if event == '-MUA-':
        Window_MUAShow()
    
# MUA Buttons

    if event == '-PosB-':
        MUA_refresh()
        MUA_Position()
        calType = 1
        conf = 1

    if event == '-VelB-':
        MUA_refresh()
        MUA_Velocity()
        calType = 2
        conf = 1
    
    if event == '-TimeB-':
        MUA_refresh()
        MUA_Time()
        calType = 3
        conf = 1
    
    if event == '-AcelB-':
        MUA_refresh()
        MUA_Aceleration()
        calType = 4
        conf = 1
    
# Specific MUA layout manipulation

    if event == '-V0c-':
        if calType == 2: # Calculo velocidad
            if conf == 1: 
                MUA_V0_Disable  (1)
                MUA_X0_Enable   (2)
                MUA_X1_Enable   (2)
                conf = 2
            elif conf == 2:
                MUA_V0_Enable   (1)
                MUA_X0_Disable  (2)
                MUA_X1_Disable  (2)
                conf = 1
            elif conf == 3:
                MUA_V0_Enable   (1)
                MUA_T_Enable    (1)
                MUA_X0_Disable  (2)
                MUA_X1_Disable  (2)
                conf = 1
        elif calType == 4: # Calculo de aceleracion
            if conf == 1:
                MUA_V0_Disable  (1)
                MUA_V1_Enable   (2)
                conf = 2
            if conf == 2:
                MUA_V0_Enable   (1)
                MUA_V1_Disable  (2)
                conf = 1 

    if event == '-Ac-':
        if conf == 1:
            MUA_A_Disable   (1)
            MUA_V0_Enable   (2)
            conf = 2
            
        elif conf == 2:
            MUA_A_Enable    (1)
            MUA_V0_Disable  (2)
            conf = 1

    if event == '-Tc-':
        if conf == 1:
            MUA_T_Disable   (1)
            MUA_X0_Enable   (2)
            MUA_X1_Enable   (2)
            metadata = 1
            conf = 3
        
        elif conf == 2:
            MUA_T_Disable   (1)
            MUA_V0_Enable   (1)
            metadata = 2
            conf = 3
        
        elif conf == 3:
            MUA_T_Enable    (1)
            if metadata == 1:
                MUA_X0_Disable  (2) 
                MUA_X1_Disable  (2)
                conf = 1
            elif metadata == 2:
                MUA_V0_Disable  (1)
                conf = 2

    if event == '-V1c-':
        if conf == 1:
            MUA_V1_Disable  (1)
            MUA_V0_Enable   (2)
            conf = 2
        elif conf == 2:
            MUA_V1_Enable   (1)
            MUA_V0_Disable  (2)
            conf = 1

# Calculate results

    if event == '-Calculate-': 
        Result = Calc(calType, conf)
        if Result == 'VNV-1':
            sg.popup_ok(f'    Algo fue mal (／ˍ・、)\n\nPorfavor revisa tus datos de entrada, revisa los signos de las entradas\n\n\n Error VNV-1', title="Tiempo negativo ?)")
        elif Result == 'VNV-2':
            if calType == 2 or calType == 4:
                sg.popup_ok(f'    Algo fue mal    ＼(º □ º l|l)/\n\nPorfavor revisa tus datos de entrada, el error puede ser causado por:\n\n - Intentaste romper el espacio tiempo, revisa la entrada del tiempo que sea diferente de 0.\n\n - ¿Ya revisaste el tiempo?, es broma, verifica que ningun dato al sumarse/restarse sea igual a 0.\n\n\n Error VNV-2', title="Ruptura Espacio-Temporal")
            elif calType == 3:
                sg.popup_ok(f'    Algo fue mal    ＼(º □ º l|l)/\n\nPorfavor revisa tus datos de entrada, el error puede ser causado por:\n\n - Intentaste romper el espacio tiempo, revisa la entrada de la aceleracion que sea diferente de 0.\n\n - ¿Ya revisaste la aceleracion?, es broma, verifica que ningun dato al sumarse/restarse sea igual a 0.\n\n\n Error VNV-2', title="Ruptura Espacio-Temporal")
        else:
            if calType == 1:
                sg.popup(f'Respuesta: {Result} m',    title = 'Respuesta')
            elif calType == 2:
                sg.popup(f'Respuesta: {Result} m/s',  title = 'Respuesta')
            elif calType == 3:
                sg.popup(f'Respuesta: {Result} s',    title = 'Respuesta')
            elif calType == 4:
                sg.popup(f'Respuesta: {Result} m/s2', title = 'Respuesta')

    if event == '-TCalculate-':
        tCalc()

    if event == '-Tray-':
        Window_TrayShow()
    
    if event == '-About-':
        sg.popup('     Universidad Nacional de Colombia\n\nProgramado por Angel Leonardo Gonzalez Padilla para la asignatura Programacion de computadores\n\n\n   Bajo la licencia WTFPL',title='Acerca de')

    if event == '-Back-' or event == '-TBack-':
        window_2Hide()
        Window_1Show()
        

    if event in (None, '-Exit-', sg.WIN_CLOSED):
        break

window.Close()
