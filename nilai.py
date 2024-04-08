def get_grade(skor):
    if 90 <= skor <= 100:
        return 'A', 'Dengan Pujian'
    elif 80 <= skor <= 89:
        return 'B', 'Sangat Memuaskan'
    elif 70 <= skor <= 79:
        return 'C', 'Memuaskan'
    elif 60 <= skor <= 69:
        return 'D', 'Tidak Memuaskan'
    elif 0 <= skor <= 59:
        return 'E', 'Tidak LULUS'
    else:
        return 'Invalid skor'

def main():
    while True:
        try:
            skor = int(input('masukan skor anda: '))
            if 0 <= skor <= 100:
                grade, predicate = get_grade(skor)
                print(f'nilai anda adalah {grade} dengan predikat {predicate}.')
                break
            else:
                print('mohon masukan nilai diantara 0 sampai 100.')
        except ValueError:
            print('Invalid input. Please enter a number.')

if __name__ == '__main__':
    main()