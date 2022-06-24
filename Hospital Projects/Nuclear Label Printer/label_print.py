from reportlab.lib.units import mm
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import sys



class GenLabel:
    
    
    def __init__(self,filename="Label.pdf", label_data=[["test_uid","test_patient_name","test_gender","test_age","test_dr_name","test_order_name"]], manual_dr_name = "External"):
        """
        @param date: The date to use
        @param amount: The amount owed
        @param receiver: The person who received the amount owed
        """
        
                 
            

        self.my_canvas = SimpleDocTemplate(filename, pagesize=(100*mm,50*mm),rightMargin=1, leftMargin=20,topMargin=1,bottomMargin=1)

        flowables = []
        
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Light", "BOOKOS.TTF"))
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Italic", "BBOOKOSI.TTF"))
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Bold Italic", "BOOKOSBI.TTF"))
        # pdfmetrics.registerFont(TTFont("Bookman Old Style Bold", "BOOKOSB.TTF"))
        
        pdfmetrics.registerFontFamily("Bookman Old Style",normal="Bookman Old Style,",bold="Bookman Old Style Bold", italic="Bookman Old Style Italic", boldItalic="Bookman Old Style Bold Italic" )
        pdfmetrics.registerFont(TTFont('Bookman Old Style','BOOKOSB.TTF'))
        

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='label',
                                  fontName="Bookman Old Style",
                                  fontSize=16,
                                  leading=12))
        styles.add(ParagraphStyle(name ="times",
                                  fontName="Bookman Old Style",
                                  fontSize = 12,
                                  leading = 12))
        for patients in label_data:

            newdata = list(patients)
            age = str(newdata[3])

            if newdata[4] == "External":
                newdata.pop(4)
                newdata.insert(4, manual_dr_name)
            
            
            if  newdata[2] == "Male":
                newdata.pop(2)
                newdata.pop(2)
                newdata.insert(2,"Male            " + age)
            
        
            elif newdata[2] == "Female":
                newdata.pop(2)
                newdata.pop(2)
                newdata.insert(2,"Female            " + age)
            
        
            else:
                pass

        
        #gen_age ="".join(newdata[2] + newdata[3])
        
        #newdata.pop(2)
        #newdata.pop(2)
        #newdata.insert(2,gen_age)

            uhid = newdata[0]
            flowables.append(Paragraph(uhid,styles["label"]))
            flowables.append(Spacer(1, 10))

            name = newdata[1]
            flowables.append(Paragraph(name,styles["label"]))
            flowables.append(Spacer(1, 10))

            gender_age = newdata[2]
            flowables.append(Paragraph(gender_age,styles["times"]))
            flowables.append(Spacer(1, 6))

            dr_name = newdata[3]
            flowables.append(Paragraph(dr_name,styles["times"]))
            flowables.append(Spacer(1, 6))

            ser_name = newdata[4]
            flowables.append(Paragraph(ser_name,styles["times"]))
            flowables.append(Spacer(1, 6))
       
            ct = datetime.datetime.now()
            ct = ct.date()
            flowables.append(Paragraph(str(ct),styles["times"]))
            flowables.append(Spacer(1, 6))
        
        self.my_canvas.build(flowables)




        #self.my_canvas.drawString(0, 10, data[0])
    
          
        


if __name__ == '__main__':

    GenLabel()

    
    # GenLabel('form.pdf', str(ct),
    # '$1,999', 'Mike')
