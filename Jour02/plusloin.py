def triangle(ab, bc, ac):
        if ab + bc > ac and bc + ac > ab and ac + ab > bc:
            print("Go get your triangle, tiger")
            if ab == bc and bc == ac and ac == ab:
                print("Tu es un triangle equilateral, Harry.")

            elif ab == ac or bc == ab or ac == bc:
                if ab**2 + bc**2 == ac**2 or ac**2 + ab**2 == bc**2 or bc**2 + ac**2 == ab**2:
                    print("Tu es un triangle rectangle isocele, Harry.")
                else:
                    print("Tu es un triangle isocele, Harry.")
            elif ab**2 + bc**2 == ac**2 or ac**2 + ab**2 == bc**2 or bc**2 + ac**2 == ab**2:
                print("Tu es un triangle rectangle, Harry.")
            else:
                print("Tu es un triangle quelconque, Harry.")
        else:
             print('Tu n\'es pas un triangle, Harry.')

triangle(1, 1, 10)