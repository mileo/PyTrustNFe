# coding=utf-8
'''
Created on Jun 14, 2015

@author: danimar
'''
import unittest
from pytrustnfe.Servidores import localizar_url

url_ba = 'https://nfe.sefaz.ba.gov.br/webservices/NfeAutorizacao/NfeAutoriza\
cao.asmx'

url_sp = 'https://nfe.fazenda.sp.gov.br/ws/nfeautorizacao.asmx'

url_sc = 'https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NfeAutorizacao.asmx'

url_rs = 'https://nfe.sefaz.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx'

url_cad_rs = 'https://cad.sefazrs.rs.gov.br/ws/cadconsultacadastro/cadcon\
sultacadastro2.asmx'

url_cad_sc = 'https://cad.svrs.rs.gov.br/ws/CadConsultaCadastro/CadConsult\
aCadastro2.asmx'


class test_servidores(unittest.TestCase):

    def test_localizar_url(self):
        url = localizar_url('NfeAutorizacao', '29', ambiente=1)
        self.assertEqual(url, url_ba)
        url = localizar_url('NfeAutorizacao', '35', ambiente=1)
        self.assertEqual(url, url_sp)
        url = localizar_url('NfeAutorizacao', '42', ambiente=1)
        self.assertEqual(url, url_sc)
        url = localizar_url('NfeAutorizacao', '43', ambiente=1)
        self.assertEqual(url, url_rs)

        url = localizar_url('NfeConsultaCadastro', '43', ambiente=2)
        self.assertEqual(url, url_cad_rs)

        url = localizar_url('NfeConsultaCadastro', '42', ambiente=2)
        self.assertEqual(url, url_cad_sc)
