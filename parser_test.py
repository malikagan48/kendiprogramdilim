import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

    def test_empty(self):
        takens =[]
        node = Parser(tokens).parse()
        self.assertEqual(node,None)

    def test_numbers(self):
        takens=[Token(TokenType.NUMBER, 51.2)]
        node= Parser(tokens).parse()
        self.assertEqual(node, NumberNode(51.2))

    def test_individual_operations(self):
        takens= [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(27),NumberNode(14)))    
        
         takens= [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(27),NumberNode(14)))   

         takens= [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(27),NumberNode(14)))

         takens= [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, divideNode(NumberNode(27),NumberNode(14)))   

    def   test_full_expression(self):
        tokens =[
             Token(TokenType.NUMBER, 27),
             Token(TokenType.PLUS),
             Token(TokenType.LPAREN),
             Token(TokenType.NUMBER, 43),
             Token(TokenType.DIVIDE),
             Token(TokenType.NUMBER, 36),
             Token(TokenType.MINUS),
             Token(TokenType.NUMBER, 48),
             Token(TokenType.MULTIPLY),
             Token(TokenType.NUMBER, 51),
         ]   

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(
            NumberNode(27),
            MultiplyNode(
                SubtractNode(
                    DivideNode(
                        NumberNode(43),
                        NumberNode(36),
                    ),
                    NumberNode(48),
                ),
                NumberNode(51),
            )
        ))        