import 'package:flutter/material.dart';
import 'dart:math';

void main() => runApp(ScientificCalculator());

class ScientificCalculator extends StatelessWidget {
  const ScientificCalculator({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Scientific Calculator',
      theme: ThemeData.dark(),
      home: CalculatorScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class CalculatorScreen extends StatefulWidget {
  const CalculatorScreen({super.key});

  @override
  _CalculatorScreenState createState() => _CalculatorScreenState();
}

class _CalculatorScreenState extends State<CalculatorScreen> {
  String _output = '0';
  String _expression = '';

  void _onButtonPressed(String value) {
    setState(() {
      if (value == 'C') {
        _output = '0';
        _expression = '';
      } else if (value == '=') {
        try {
          final result = _evaluateExpression(_expression);
          _output = result.toString();
        } catch (e) {
          _output = 'Error';
        }
      } else if (value == 'DEL') {
        if (_expression.isNotEmpty) {
          _expression = _expression.substring(0, _expression.length - 1);
          _output = _expression.isEmpty ? '0' : _expression;
        }
      } else {
        if (_output == '0' && value != '.') {
          _expression = value;
        } else {
          _expression += value;
        }
        _output = _expression;
      }
    });
  }

  double _evaluateExpression(String expression) {
    expression = expression.replaceAll(' ', '');

    expression = expression.replaceAllMapped(
      RegExp(r'sin\((.*?)\)'),
      (match) => sin(_toRadians(double.parse(match.group(1)!))).toString(),
    );
    expression = expression.replaceAllMapped(
      RegExp(r'cos\((.*?)\)'),
      (match) => cos(_toRadians(double.parse(match.group(1)!))).toString(),
    );
    expression = expression.replaceAllMapped(
      RegExp(r'tan\((.*?)\)'),
      (match) => tan(_toRadians(double.parse(match.group(1)!))).toString(),
    );

    final tokens = RegExp(r'(\d+(\.\d+)?|[\+\-\*/\^\(\)])')
        .allMatches(expression)
        .map((m) => m.group(0)!)
        .toList();

    final numbers = <double>[];
    final operators = <String>[];

    int precedence(String operator) {
      if (operator == '+' || operator == '-') return 1;
      if (operator == '*' || operator == '/') return 2;
      if (operator == '^') return 3;
      return 0;
    }

    void applyOperator() {
      if (numbers.length < 2 || operators.isEmpty) return;
      final b = numbers.removeLast();
      final a = numbers.removeLast();
      final op = operators.removeLast();

      switch (op) {
        case '+':
          numbers.add(a + b);
          break;
        case '-':
          numbers.add(a - b);
          break;
        case '*':
          numbers.add(a * b);
          break;
        case '/':
          if (b == 0) throw Exception("Division by zero");
          numbers.add(a / b);
          break;
        case '^':
          numbers.add(pow(a, b).toDouble());
          break;
        default:
          throw Exception("Unknown operator: $op");
      }
    }

    for (final token in tokens) {
      if (double.tryParse(token) != null) {
        numbers.add(double.parse(token));
      } else if (token == '(') {
        operators.add(token);
      } else if (token == ')') {
        while (operators.isNotEmpty && operators.last != '(') {
          applyOperator();
        }
        operators.removeLast();
      } else {
        while (operators.isNotEmpty &&
            precedence(operators.last) >= precedence(token)) {
          applyOperator();
        }
        operators.add(token);
      }
    }

    while (operators.isNotEmpty) {
      applyOperator();
    }

    return numbers.isEmpty ? 0 : numbers.last;
  }

  double _toRadians(double degrees) {
    return degrees * (pi / 180);
  }

  Widget _buildButton(String value, Color color) {
    return GestureDetector(
      onTap: () => _onButtonPressed(value),
      child: Container(
        margin: const EdgeInsets.all(8.0),
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(10.0),
          boxShadow: const [
            BoxShadow(
              color: Colors.black38,
              offset: Offset(2, 2),
              blurRadius: 5.0,
            ),
          ],
        ),
        child: Center(
          child: Text(
            value,
            style: const TextStyle(
                color: Colors.white,
                fontSize: 22.0,
                fontWeight: FontWeight.bold),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        title: const Text('Scientific Calculator'),
        centerTitle: true,
        backgroundColor: Colors.blueGrey[900],
      ),
      body: Column(
        children: [
          Container(
            alignment: Alignment.centerRight,
            padding: const EdgeInsets.all(20.0),
            height: size.height * 0.2,
            color: Colors.black87,
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Text(
                _output,
                style: const TextStyle(
                    fontSize: 48.0,
                    color: Colors.white,
                    fontWeight: FontWeight.w400),
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
              ),
            ),
          ),
          Expanded(
            child: GridView.count(
              crossAxisCount: 4,
              padding: const EdgeInsets.all(10.0),
              children: [
                ...['7', '8', '9', '/']
                    .map((value) => _buildButton(value, Colors.grey[800]!)),
                ...['4', '5', '6', '*']
                    .map((value) => _buildButton(value, Colors.grey[800]!)),
                ...['1', '2', '3', '-']
                    .map((value) => _buildButton(value, Colors.grey[800]!)),
                ...['C', '0', '=', '+']
                    .map((value) => _buildButton(value, Colors.blueGrey[700]!)),
                ...['DEL', '(', ')', '.']
                    .map((value) => _buildButton(value, Colors.redAccent)),
                ...['^', 'sin', 'cos', 'tan']
                    .map((value) => _buildButton(value, Colors.orange)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
