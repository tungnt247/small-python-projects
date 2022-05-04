class BitmapMessage:
    DEFATULT_BITMAP = '''
    ....................................................................
       **************   *  *** **  *      ******************************
      ********************* ** ** *  * ****************************** *
     **      *****************       ******************************
              *************          **  * **** ** ************** *
               *********            *******   **************** * *
                ********           ***************************  *
       *        * **** ***         *************** ******  ** *
                   ****  *         ***************   *** ***  *
                     ******         *************    **   **  *
                     ********        *************    *  ** ***
                       ********         ********          * *** ****
                       *********         ******  *        **** ** * **
                       *********         ****** * *           *** *   *
                         ******          ***** **             *****   *
                         *****            **** *            ********
                        *****             ****              *********
                        ****              **                 *******   *
                        ***                                       *    *
                        **     *                    *
    ....................................................................
    '''

    def execute(self):
        print('Bitmap Message, by Al Sweigart al@inventwithpython.com\n')
        user_input = input('Enter the message to display with the bitmap.\n>')
        if user_input == '':
            return

        for line in BitmapMessage.DEFATULT_BITMAP.splitlines():
            for idx, char  in enumerate(line):
                if char == ' ':
                    print(' ', end='')
                else:
                    print(user_input[idx % len(user_input)], end='')
            print()

if __name__ == "__main__":
    bitmap_message = BitmapMessage()
    bitmap_message.execute()
