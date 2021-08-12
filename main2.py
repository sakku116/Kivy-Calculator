from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import math

Window.size = (270, 540)
Builder.load_file('calc_design.kv')

class CalcLayout(Widget):
    def clear(self):
        self.ids.output_label.text = ''
        self.ids.output_history.text = ''
        self.ids.output_label.font_size = 30

    def delete(self):
        output = self.ids.output_label.text
        if 'ERROR' in output:
            self.ids.output_label.text = ''
        else:
            # menghapus karakter terakhir
            output = output[:-1]
            self.ids.output_label.text = output

    def button_press(self, char):
        # Menagkap teks dari outputlabel
        output = self.ids.output_label.text
        #print(len(output))
        if 'ERROR' in output:
            self.ids.output_label.text = ''
            self.ids.output_label.text += f'{char}'
        else:
            if char == '√':
                if ')' in output:
                    if self.ids.output_label.text[-1] == ')':
                        i = list(output)
                        i.insert(len(output)-2, str(char)) 
                        self.ids.output_label.text = ''.join(i)

                else:
                    self.ids.output_label.text += f'{char}()'
            else:
                if self.ids.output_label.text[-1] == ')':
                    i = list(output)
                    i.insert(len(output)-2, str(char)) 
                    self.ids.output_label.text = ''.join(i)
                    
                else:
                    self.ids.output_label.text += f'{char}'
        print(self.ids.output_label.text.find(')'))
    
    def equals_button(self):
        pre_output = self.ids.output_label.text
        self.ids.output_history.text = pre_output
        output = pre_output.replace(',','')
        # me replace semua karakter yang ada di dictionary
        #################################
        replace_chars = {"×": "*",
            "÷":"/",
            "^":"**",}
        for i, j in replace_chars.items():
            output = output.replace(i, j)
        #################################
        '''
        try:
            # menyelesaikan masalah sqrt
            ################################
            if '√' in output:
                sqrt_index = output.find('√')
                def sqrt_float_handler(num):
                    if '.' in output: 
                        return str(math.sqrt(float(num)))
                    else:
                        return str(math.sqrt(eval(num)))

                if sqrt_index == 0:
                    remove_sqrt = output.replace('√', '')
                    print(f'number without sqrt: {remove_sqrt}')
                    output = sqrt_float_handler(remove_sqrt)

                else:
                    # memisah antara soal sebelum sqrt dan setelah sqrt dan menghilangkan sqrt
                    splited_sqrt_output = output.split('√')
                    print(f'splited_sqrt_output: {splited_sqrt_output}')
                    # menyelesaikan masalah setelah sqrt
                    sqrt_solver = sqrt_float_handler(splited_sqrt_output[1])
                    # mengganti soal setelah sqrt dengan jawaban masalah sqrt
                    splited_sqrt_output[1] = sqrt_solver
                    print(f'splited_sqrt_output after solved: {splited_sqrt_output}')
                    # menggabungkan kedua soal dengan beberapa kondisi
                    op_index = output[sqrt_index-1]
                    print(f'char before sqrt: {op_index}')
                    if op_index == '-' or op_index == '+' or op_index == '*' or op_index == '**' or op_index == '/' or op_index == '%':
                        print('ada operator')
                        output = ''.join(splited_sqrt_output)
                    else:
                        print('tidak ada operator')
                        output = '*'.join(splited_sqrt_output)
            else:
                pass
            print(f'output string: {output}')
            ###################################

            result = str(eval(output)).replace('.0','')
            if '.' in result:
                formating_float_result = result.split('.')
                formating_float_result[0] = f"{int(formating_float_result[0]):,}"
                result = '.'.join(formating_float_result)
                self.ids.output_label.text = str(result)

            else:
                result = f"{int(result):,}"
                self.ids.output_label.text = str(result)
        '''

        if '√' in output:
            print(output.split('√'))
            def sqrtmath_solver(get):
                output = get
                # mencari index √ dari output
                find_sqrt = output.find('√')
                # mendapatkan string setelah tanda sqrt dari output
                str_aft_sqrt = output[find_sqrt+1:]
                # menyelesaikan masalah sqrt di str_aft_sqrt
                sqrt_solver = math.sqrt(int(str_aft_sqrt))
                # mereplace str_aft_sqrt dengan sqrt_solver
                output = output.replace(str_aft_sqrt, str(sqrt_solver))
                if '+' in output[find_sqrt-2:find_sqrt]:
                    output = output.replace('√','')
                    return output
                else:
                    output = output.replace('√','*')
                    return output
            sqrt_output = sqrtmath_solver(output)
            result = str(eval(sqrt_output)).replace('.0','')
            
            print(f'{output} = {result}')
                


class MyCalcApp(App):
    def build(self):
        return CalcLayout()
if __name__ == '__main__':
    MyCalcApp().run()
