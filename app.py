import streamlit as st
import signal
import sys
from utils.logging import logger, flush

# Configuración de la página
st.set_page_config(page_title="Clase de Cómputo en la Nube")

def shutdown_handler(signal_int, frame):
    logger.info(f"Caught Signal {signal.strsignal(signal_int)}")
    flush()
    sys.exit(0)

# Manejo de señales (útil para Cloud Run)
signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

def main():
    # 1. Logs personalizados como tenías antes
    logger.info(logField="custom-entry", arbitraryField="custom-entry")
    logger.info("Child logger with trace Id.")

    # 2. El contenido visual (lo que antes era el return string)
    st.title("Holaaaaaa, Charly")
    st.header("desde la clase de Computo en la nube :)")
    
    st.write("Esta es una página generada con Streamlit en lugar de texto plano.")
    
    # Ejemplo de interactividad (algo que Flask no hace fácil)
    if st.button('Saludar al log'):
        logger.info("El usuario hizo clic en el botón")
        st.success("¡Saludo enviado al log!")

if __name__ == "__main__":
    main()