Attribute VB_Name = "Module1"
Sub stocks()

'Run the following conditions for all sheets

Dim ws As Worksheet

For Each ws In Worksheets
    ws.Range("I1").Value = "Ticker"
    ws.Range("J1").Value = "Yearly Change"
    ws.Range("K1").Value = "Percent Change"
    ws.Range("L1").Value = "Total Stock Volume"
    
    Dim Summary_Row As LongLong
    Dim total As LongLong
    Dim change As LongLong
    Dim percentchange As LongLong
        
    Start = 2
    Summary_Row = 2
    
    lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row

    For i = Start To lastrow
    
        starting_open = ws.Cells(Start, 3)
        closing = ws.Cells(i, 6).Value
        volume = ws.Cells(i, 7).Value
        
        If ws.Cells(i + 1, 1).Value = ws.Cells(i, 1).Value Then
           
           total = total + volume
        
        
        Else
             
            total = total + volume
            change = (closing - starting_open)
            
                If starting_open = 0 Or IsEmpty(starting_open) Then
                    starting_open = Null
                Else
                      percentchange = Round((change / starting_open * 100), 2)
                End If
    
        
            'percentchange = Round((change / starting_open * 100), 2)
            
            Start = i + 1
            
            ws.Range("I" & Summary_Row).Value = ws.Cells(i, 1).Value
            ws.Range("J" & Summary_Row).Value = Round(change, 2)
            ws.Range("K" & Summary_Row).Value = "%" & percentchange
            ws.Range("L" & Summary_Row).Value = total
            
            
            total = 0
            change = 0
            Summary_Row = Summary_Row + 1
            
            
            
        End If
        
    Next i
    
lastrow_final = ws.Cells(Rows.Count, "J").End(xlUp).Row
    For K = 2 To lastrow_final
        If ws.Cells(K, "J").Value < 0 Then
            ws.Cells(K, "J").Interior.ColorIndex = 3
    Else
        ws.Cells(K, "J").Interior.ColorIndex = 4
    End If
Next K
    
 
    
Next ws

MsgBox ("DONE?!?!")


End Sub

