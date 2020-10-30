import sys
sys.path.append("..") 

from src.cita import Cita

import pytest

@pytest.fixture
def cita(): 
    return Cita("UnID","fecha","hora","pelado","tiempo","precio")

def test_cogerCita():
	assert cita.getFecha() == "" 
	assert cita.getHora() == "" 
	assert cita.getPelado() == "" 
	
def test_modificarCita():
	assert cita.getFecha() == "" 
	assert cita.getHora() == "" 	

def test_getID(): 
    assert cita.getID() == ""

def test_getFecha():
    assert cita.getFecha() == ""

def test_getHora(): 
    assert cita.getHora() == ""

def test_getPelado(): 
    assert cita.getPelado() == ""

def test_getTiempo():
    assert cita.getTiempo() == ""

def test_getPrecio():
    assert cita.getPrecio() == ""

