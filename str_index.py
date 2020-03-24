"""
HTML_INDEX_PAGE: str
uso:

HTML_INDEX_PAGE.format()
"""


HTML_INDEX_PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="120">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://kit.fontawesome.com/a80232805f.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="style.css">
    <title>COVID-19 | Mundo & Brasil</title>
</head>
<body>
    

    <div class="titulo" ><h1> <i class="fas fa-terminal blink_me"></i> COVID-19 | CORONAVÍRUS | MONITOR</h1> </div>  

    <div = class="conteudo-left">
        <h2 class="titulo-tabela selecionar">MUNDO</h2>
        <h2 class="titulo-tabela"> ----------- </h2>
        <table border="0" class="tabela">
            <tr class="selecionar">
                <td>CASOS</td>
                <td class="direita">{}</td>
            </tr>
            <tr class="selecionar">
                <td>MORTES </td>
                <td class="direita cor-vermelho">{}</td> 
            </tr>
            <tr class="selecionar">
                <td>RECUPERADOS</td>
                <td class="direita cor-verde">{}</td> 
            </tr>
            <tr class="selecionar">
                <td>TAXA DE LETALIDADE <i class="fas fa-skull-crossbones"></i> </td>
                <td class="direita">{}%</td> 
            </tr>
            <tr class="selecionar">
                <td>TAXA RECUPERADOS</td>
                <td class="direita">{}%</td> 
            </tr>
        </table>
    
    </div>


    <div = class="conteudo-right">
        <h2 class="titulo-tabela selecionar">BRASIL</h2>
        <h2 class="titulo-tabela"> ----------- </h2>
        <table border="0">
            <tr class="selecionar">
                <td>CASOS</td>
                <td class="direita">{}</td> 
            </tr>
            <tr class="selecionar">
                <td>MORTES</td>
                <td class="direita cor-vermelho">{}</td> 
            </tr>
            <tr class="selecionar">
                <td>RECUPERADOS</td>
                <td class="direita cor-verde">{}</td> 
            </tr>
            <tr class="selecionar">
                <td>TAXA DE LETALIDADE <i class="fas fa-skull-crossbones"></i> </td>
                <td class="direita">{}%</td> 
            </tr>
            <tr class="selecionar">
                <td>TAXA DE RECUPERADOS </td>
                <td class="direita">{}%</td> 
            </tr>
        </table>
    </div>

    <footer class="footer">
        <div class="selecionar">  última atualização: {} </div>
       jhoonb: <a href="https://www.twitter.com/jhoonb"> <i class="fab fa-twitter"></i> </i></a>
            
        <a href="https://www.github.com/jhoonb"> <i class="fab fa-github"></i></a>

        <a href="http://telegram.me/jhoonb"> <i class="fab fa-telegram"></i></a>

        <a href="https://discordapp.com/"> <i class="fab fa-discord"></i></a>

        <a href="https://medium.com/@jhoonb"> <i class="fab fa-medium"></i></a>

        <a href="https://dev.to/jhoonb"> <i class="fab fa-dev"></i></a> 
        <br>
        <i class="fas fa-code"></i>
        <a href="https://github.com/jhoonb/corona" class="btn btn-default">Source Code</a>
        <i class="fas fa-code"></i>
        
        
      </footer>
</body>
</html>'''