import sys
sys.path.append("..") 

from src.cita import Cita

import pytest

@pytest.fixture
def cita():
    return Cita("UnID","fecha","hora","pelado","tiempo","precio")

    
