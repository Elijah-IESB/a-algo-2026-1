"""Gera o PDF do dever sobre Heap Maxima."""

import math
from dataclasses import dataclass

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ARQUIVO_SAIDA = "heap_maxima_passo_a_passo.pdf"
ELEMENTOS = [13, 2, 6, 25, 8, 40, 1]


@dataclass
class Etapa:
    """Representa uma etapa visual da construcao ou remocao da heap."""

    titulo: str
    descricao: str
    comparacoes: list[str]
    trocas: list[str]
    heap: list[int]


class DesenhoHeap(Flowable):
    """Desenha uma heap em formato de arvore."""

    def __init__(self, heap, largura=23 * cm, altura=5.9 * cm):
        super().__init__()
        self.heap = heap
        self.width = largura
        self.height = altura

    def draw(self):
        if not self.heap:
            self.canv.setFillColor(colors.HexColor("#555555"))
            self.canv.setFont("Helvetica", 11)
            self.canv.drawCentredString(self.width / 2, self.height / 2, "Heap vazia")
            return

        niveis = math.floor(math.log2(len(self.heap))) + 1
        margem_x = 0.8 * cm
        topo = self.height - 0.7 * cm
        espaco_y = min(1.65 * cm, (self.height - 1.2 * cm) / max(niveis - 1, 1))
        raio = 0.36 * cm
        posicoes = {}

        for indice, valor in enumerate(self.heap):
            nivel = math.floor(math.log2(indice + 1))
            posicao_nivel = indice - (2**nivel - 1)
            quantidade_nivel = 2**nivel
            largura_util = self.width - 2 * margem_x
            passo_x = largura_util / quantidade_nivel
            x = margem_x + passo_x * (posicao_nivel + 0.5)
            y = topo - nivel * espaco_y
            posicoes[indice] = (x, y)

        self.canv.setStrokeColor(colors.HexColor("#9AA4B2"))
        self.canv.setLineWidth(1.1)

        for indice in range(1, len(self.heap)):
            pai = (indice - 1) // 2
            x1, y1 = posicoes[pai]
            x2, y2 = posicoes[indice]
            self.canv.line(x1, y1 - raio, x2, y2 + raio)

        for indice, valor in enumerate(self.heap):
            x, y = posicoes[indice]
            self.canv.setFillColor(colors.HexColor("#0B5CAD"))
            self.canv.setStrokeColor(colors.HexColor("#0A2540"))
            self.canv.circle(x, y, raio, fill=1, stroke=1)
            self.canv.setFillColor(colors.white)
            self.canv.setFont("Helvetica-Bold", 10)
            self.canv.drawCentredString(x, y - 3, str(valor))


def inserir_elemento(heap, elemento):
    """Insere um elemento na heap maxima e registra comparacoes e trocas."""
    heap.append(elemento)
    indice = len(heap) - 1
    comparacoes = []
    trocas = []

    while indice > 0:
        pai = (indice - 1) // 2
        comparacoes.append(
            f"Compara filho {heap[indice]} com pai {heap[pai]}."
        )

        if heap[indice] > heap[pai]:
            trocas.append(f"Swap: {heap[indice]} troca com {heap[pai]}.")
            heap[indice], heap[pai] = heap[pai], heap[indice]
            indice = pai
        else:
            comparacoes.append("Como o filho nao e maior que o pai, para a subida.")
            break

    if not trocas:
        trocas.append("Nenhuma troca foi necessaria.")

    return comparacoes, trocas


def remover_maior(heap):
    """Remove o maior elemento da heap e registra a reorganizacao."""
    removido = heap[0]
    comparacoes = [f"Remove o maior elemento: {removido}."]
    trocas = []

    ultimo = heap.pop()

    if heap:
        heap[0] = ultimo
        comparacoes.append(f"Move o ultimo elemento ({ultimo}) para a raiz.")
    else:
        comparacoes.append("A heap ficou vazia apos a remocao.")
        return removido, comparacoes, ["Nenhuma troca foi necessaria."]

    indice = 0

    while True:
        esquerda = 2 * indice + 1
        direita = 2 * indice + 2
        maior = indice

        if esquerda < len(heap):
            comparacoes.append(
                f"Compara pai {heap[indice]} com filho esquerdo {heap[esquerda]}."
            )
            if heap[esquerda] > heap[maior]:
                maior = esquerda

        if direita < len(heap):
            comparacoes.append(
                f"Compara maior atual {heap[maior]} com filho direito {heap[direita]}."
            )
            if heap[direita] > heap[maior]:
                maior = direita

        if maior == indice:
            comparacoes.append("A propriedade de Max Heap foi restaurada.")
            break

        trocas.append(f"Swap: {heap[indice]} troca com {heap[maior]}.")
        heap[indice], heap[maior] = heap[maior], heap[indice]
        indice = maior

    if not trocas:
        trocas.append("Nenhuma troca foi necessaria.")

    return removido, comparacoes, trocas


def montar_etapas():
    """Monta todas as etapas de insercao e remocao."""
    etapas_insercao = []
    etapas_remocao = []
    heap = []

    for elemento in ELEMENTOS:
        comparacoes, trocas = inserir_elemento(heap, elemento)
        etapas_insercao.append(
            Etapa(
                titulo=f"Insercao do elemento {elemento}",
                descricao=f"Elemento inserido no fim da fila e ajustado para manter a Max Heap.",
                comparacoes=comparacoes,
                trocas=trocas,
                heap=heap.copy(),
            )
        )

    while heap:
        removido, comparacoes, trocas = remover_maior(heap)
        etapas_remocao.append(
            Etapa(
                titulo=f"Remocao do maior elemento: {removido}",
                descricao="A raiz e removida, o ultimo elemento sobe para a raiz e a heap desce ate reorganizar.",
                comparacoes=comparacoes,
                trocas=trocas,
                heap=heap.copy(),
            )
        )

    return etapas_insercao, etapas_remocao


def lista_para_texto(itens):
    """Transforma uma lista de eventos em texto com quebras."""
    return "<br/>".join(f"- {item}" for item in itens)


def tabela_resumo(etapa, estilos):
    """Cria o bloco textual de uma etapa."""
    dados = [
        [
            Paragraph("<b>Comparacoes realizadas</b>", estilos["TabelaCabecalho"]),
            Paragraph("<b>Trocas realizadas</b>", estilos["TabelaCabecalho"]),
            Paragraph("<b>Heap em vetor</b>", estilos["TabelaCabecalho"]),
        ],
        [
            Paragraph(lista_para_texto(etapa.comparacoes), estilos["TabelaTexto"]),
            Paragraph(lista_para_texto(etapa.trocas), estilos["TabelaTexto"]),
            Paragraph(str(etapa.heap), estilos["TabelaTextoCentro"]),
        ],
    ]

    tabela = Table(dados, colWidths=[9.2 * cm, 7.2 * cm, 6.2 * cm])
    tabela.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9EAF7")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#12324A")),
                ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#9FB6C8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    return tabela


def criar_estilos():
    """Cria os estilos usados no PDF."""
    estilos = getSampleStyleSheet()
    estilos.add(
        ParagraphStyle(
            name="TituloPrincipal",
            parent=estilos["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=28,
            textColor=colors.HexColor("#0A2540"),
            alignment=TA_CENTER,
            spaceAfter=12,
        )
    )
    estilos.add(
        ParagraphStyle(
            name="Subtitulo",
            parent=estilos["Normal"],
            fontSize=12,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#334155"),
            spaceAfter=18,
        )
    )
    estilos.add(
        ParagraphStyle(
            name="Secao",
            parent=estilos["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=20,
            textColor=colors.HexColor("#0B5CAD"),
            spaceBefore=10,
            spaceAfter=8,
        )
    )
    estilos.add(
        ParagraphStyle(
            name="EtapaTitulo",
            parent=estilos["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            textColor=colors.HexColor("#12324A"),
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    estilos.add(
        ParagraphStyle(
            name="Texto",
            parent=estilos["Normal"],
            fontSize=9.5,
            leading=12.5,
            textColor=colors.HexColor("#1F2937"),
            spaceAfter=5,
        )
    )
    estilos.add(
        ParagraphStyle(
            name="TabelaCabecalho",
            parent=estilos["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.4,
            leading=10.5,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#12324A"),
        )
    )
    estilos.add(
        ParagraphStyle(
            name="TabelaTexto",
            parent=estilos["Normal"],
            fontSize=7.7,
            leading=9.5,
            textColor=colors.HexColor("#1F2937"),
        )
    )
    estilos.add(
        ParagraphStyle(
            name="TabelaTextoCentro",
            parent=estilos["TabelaTexto"],
            alignment=TA_CENTER,
        )
    )
    return estilos


def cabecalho(canvas_pdf: canvas.Canvas, documento):
    """Adiciona rodape com numeracao de paginas."""
    canvas_pdf.saveState()
    canvas_pdf.setFont("Helvetica", 8)
    canvas_pdf.setFillColor(colors.HexColor("#64748B"))
    canvas_pdf.drawRightString(
        documento.pagesize[0] - 1.3 * cm,
        0.8 * cm,
        f"Pagina {documento.page}",
    )
    canvas_pdf.restoreState()


def adicionar_etapas(elementos, etapas, estilos):
    """Adiciona as etapas ao documento."""
    for indice, etapa in enumerate(etapas, start=1):
        bloco = [
            Paragraph(f"{indice}. {etapa.titulo}", estilos["EtapaTitulo"]),
            Paragraph(etapa.descricao, estilos["Texto"]),
            DesenhoHeap(etapa.heap),
            Spacer(1, 0.18 * cm),
            tabela_resumo(etapa, estilos),
            Spacer(1, 0.38 * cm),
        ]
        elementos.append(KeepTogether(bloco))


def gerar_pdf():
    """Gera o arquivo PDF final."""
    estilos = criar_estilos()
    etapas_insercao, etapas_remocao = montar_etapas()
    documento = SimpleDocTemplate(
        ARQUIVO_SAIDA,
        pagesize=landscape(A4),
        rightMargin=1.2 * cm,
        leftMargin=1.2 * cm,
        topMargin=1.1 * cm,
        bottomMargin=1.2 * cm,
    )

    elementos = [
        Paragraph("Max Heap - Fila de Prioridade", estilos["TituloPrincipal"]),
        Paragraph(
            "Fluxo completo de insercao e remocao dos elementos "
            "[13, 2, 6, 25, 8, 40, 1].",
            estilos["Subtitulo"],
        ),
        Paragraph("Objetivo", estilos["Secao"]),
        Paragraph(
            "Ilustrar como uma Heap Maxima organiza os elementos para que o "
            "maior valor fique sempre na raiz, permitindo a remocao do item "
            "de maior prioridade.",
            estilos["Texto"],
        ),
        Paragraph("Insercoes na Heap", estilos["Secao"]),
    ]

    adicionar_etapas(elementos, etapas_insercao, estilos)
    elementos.append(PageBreak())
    elementos.append(Paragraph("Remocoes do Elemento de Maior Prioridade", estilos["Secao"]))
    adicionar_etapas(elementos, etapas_remocao, estilos)

    documento.build(elementos, onFirstPage=cabecalho, onLaterPages=cabecalho)


if __name__ == "__main__":
    gerar_pdf()
