# MegaETH Tools

MegaETH testnet için otomatik işlem araçları. Bu araçlar aşağıdaki işlemleri gerçekleştirebilir:

- GTE Faucet'ten token talep etme
- CAP token'larını mint etme
- Teko Finance token'larını mint etme (tkETH, tkUSDC, tkWBTC)
- Bebop Exchange üzerinde token takası yapma
- GTE Exchange üzerinde token takası yapma

## Kurulum

1. Repository'yi klonlayın:
```bash
git clone https://github.com/getcakedieyoungx/megaeth-tools.git
cd megaeth-tools
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. `config.json` dosyasında gerekli ayarlamaları yapın:
- RPC URL
- Contract adresleri
- Gas ayarları
- Gecikme süreleri

2. Programı çalıştırın:
```bash
python main.py
```

3. Private key'inizi girin ve işlemlerin otomatik olarak gerçekleşmesini bekleyin.

## Güvenlik

- Private key'inizi güvenli bir şekilde saklayın
- Private key'inizi asla başkalarıyla paylaşmayın
- İşlemler sırasında yeterli bakiyeniz olduğundan emin olun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.