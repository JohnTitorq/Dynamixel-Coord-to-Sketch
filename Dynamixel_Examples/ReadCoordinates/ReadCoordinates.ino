#include <Dynamixel2Arduino.h>  // подключение библиотеки Dynamixel. Для работы с нашими проводами вы можете ее скачать с нашего сайта
#define DXL_SERIAL   Serial3 // OpenCM9.04 EXP Board's DXL port Serial. (To use the DXL port on the OpenCM 9.04 board, you must use Serial1 for Serial. And because of the OpenCM 9.04 driver code, you must call Serial1.setDxlMode(true); before dxl.begin();.)
#define DEBUG_SERIAL Serial  // Установка константы, отвечающей за последовательный порт, подключаемый к компьютеру
const uint8_t DXL_DIR_PIN = 22; // инициализация переменной, отвечающей за номер пина, подключенного к информационному пину сервоприводов манипулятора
const float DXL_PROTOCOL_VERSION = 1.0;   // инициализация переменной, отвечающей за протокол передачи данных от OpenCM9.04 к сервоприводам

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN); // инициализация указателя на команды из библиотеки Dynamixel

#define jointN 6         // инициализация константы, обозначающей количество сервоприводов (и, соответственно, элементов массива)
int pos=0;                 // инициализация переменной pos
int i=0;                   // инициализация переменной i
int buf[jointN+1];         // инициализация одномерного массива, его размер задается 5+1=7, так как в программировании нумерация
                           // элементов начинается с 0, но нулевой элемент мы использовать не будем, в связи с чем начнем с первого

void setup() {
  
  DEBUG_SERIAL.begin(57600); // установка скорости обмена данными по последовательному порту компьютера
  dxl.begin(1000000);        // установка скорости обмена данными по последовательному порту манипулятора
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);   // выбор протокола обмена данными
  for (i=1; i<jointN+1; i++)   // цикл с изменением i от 1 до 5 с шагом 1
  {
      dxl.setOperatingMode(i, OP_POSITION);  // установка режима работы сервопривода с номером i в качестве шарнира
  }
}

void loop() {
  
  for (i=1; i<=jointN; i++) // цикл с изменением i от 1 до 5 с шагом 1
  {
    pos = dxl.getPresentPosition(i);  // получение текущей позиции привода с номером i и запись в переменную pos
    buf[i]=pos;  // запись переменной значения pos в i-тый элемент массива buf 
    //Serial.println(buf[i]);
  }

  Serial.print("{ "); //вывод в монитор порта текста "{ "
  for (i=1; i<=jointN; i++) // цикл с изменением i от 1 до 5 с шагом 1
  {
    Serial.print(buf[i]); // вывод в монитор порта значения ячейки массива с номером i
    Serial.print(", "); // вывод в монитор порта текста ", "
  }
  Serial.print("}, "); // вывод в монитор порта текста "}, "
  Serial.println(' '); // вывод в монитор порта текста " " и перенос курсора на следующую строку

  delay(1000);          // задержка, пауза в 1 секунду
  
}
