from deep_translator import GoogleTranslator
from gtts import gTTS

text='''The platform was nearly empty when Aarav arrived, his breath curling in the cold night air.The last train to Mirapur stood waiting, its windows glowing faintly like tired eyes. He clutched a small leather suitcase—everything he owned now fit inside it. As he stepped aboard, the carriage seemed older than time itself, the wood polished by countless hands, the air thick with the scent of rain and rust. Across from him sat an old woman in a crimson shawl, her gaze fixed on him with unsettling familiarity. “You’re late,” she said softly, as if she had been expecting him for years. Aarav’s heart quickened. He had never seen her before, yet her voice felt like a memory he had misplaced. Outside, the train began to move, and with each passing mile, the world beyond the windows grew stranger—fields of silver grass, rivers that flowed upward, and skies painted in colors he had no name for. Aarav realized this was no ordinary journey;
\the train wasn’t taking him to Mirapur—it was taking him somewhere he had once promised to return.'''
tcode=GoogleTranslator(source="en",target="gu").translate(text)
print(tcode)

voice=gTTS(text=tcode,lang="gu")
voice.save("myvoice.mp3")

print("Voice File Saved ")
