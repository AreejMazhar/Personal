Module Module1

    Sub Main()
        Dim Pass As String
        Dim Valid As Boolean

        Console.Write("Enter Your Password: ")
        Pass = Console.ReadLine()

        Valid = ValidatePassword(Pass)

        If (Valid = True) Then
            Console.WriteLine("Your Password is Valid")
            Console.ReadKey()
        Else
            Console.WriteLine("Your Password is Invalid")
            Console.ReadKey()

        End If

    End Sub

    Function ValidatePassword(ByVal Pass As String) As Boolean
        Dim i As Integer
        Dim NextChar As Char
        Dim LC As Integer
        Dim UC As Integer
        Dim Num As Integer
        Dim SC As Integer
        Dim Flag As Boolean

        Flag = False
        LC = 0
        UC = 0
        Num = 0
        SC = 0


        For i = 1 To Len(Pass)
            NextChar = Mid(Pass, i, 1)
            If (NextChar >= "a") And (NextChar <= "z") Then
                LC = LC + 1
            ElseIf (NextChar >= "A") And (NextChar <= "Z") Then
                UC = UC + 1
            ElseIf (NextChar >= "0") And (NextChar <= "9") Then
                Num = Num + 1
            Else
                SC = SC + 1
            End If
        Next

        If (LC >= 2) And (UC >= 2) And (Num >= 3) And (SC = 0) Then
            Flag = True
        Else
            Flag = False
        End If

        Return Flag

    End Function


End Module
