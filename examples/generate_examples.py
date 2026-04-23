"""
生成示例星座图供学生参考
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def create_example_constellations():
    """创建示例星座图"""
    
    # 创建examples目录
    os.makedirs('../examples', exist_ok=True)
    
    # BPSK示例
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    bpsk_symbols = np.array([-1, 1])
    ax.scatter(np.real(bpsk_symbols), np.imag(bpsk_symbols), 
               s=200, c='blue', marker='o', alpha=0.7, edgecolors='black', linewidths=2)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('实部 (In-phase)', fontsize=12)
    ax.set_ylabel('虚部 (Quadrature)', fontsize=12)
    ax.set_title('BPSK星座图（示例）', fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    
    # 标注符号
    ax.text(-1, -0.2, '比特1', ha='center', fontsize=10)
    ax.text(1, -0.2, '比特0', ha='center', fontsize=10)
    
    plt.savefig('../examples/bpsk_constellation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ BPSK示例已生成")
    
    # QPSK示例
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    qpsk_symbols = np.array([
        (1 + 1j) / np.sqrt(2),
        (-1 + 1j) / np.sqrt(2),
        (-1 - 1j) / np.sqrt(2),
        (1 - 1j) / np.sqrt(2)
    ])
    ax.scatter(np.real(qpsk_symbols), np.imag(qpsk_symbols), 
               s=200, c='red', marker='s', alpha=0.7, edgecolors='black', linewidths=2)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlabel('实部 (In-phase)', fontsize=12)
    ax.set_ylabel('虚部 (Quadrature)', fontsize=12)
    ax.set_title('QPSK星座图（示例）', fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    
    # 标注符号
    labels = ['00', '01', '11', '10']
    for sym, label in zip(qpsk_symbols, labels):
        offset = 0.15
        ax.text(np.real(sym) + offset * np.sign(np.real(sym)), 
               np.imag(sym) + offset * np.sign(np.imag(sym)), 
               label, ha='center', fontsize=10, 
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.savefig('../examples/qpsk_constellation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ QPSK示例已生成")
    
    # 16-QAM示例
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    # 生成16-QAM符号
    levels = np.array([-3, -1, 1, 3])
    qam16_symbols = []
    for i in levels:
        for q in levels:
            qam16_symbols.append((i + 1j * q) / np.sqrt(10))
    qam16_symbols = np.array(qam16_symbols)
    
    ax.scatter(np.real(qam16_symbols), np.imag(qam16_symbols), 
               s=150, c='green', marker='o', alpha=0.7, edgecolors='black', linewidths=2)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlabel('实部 (In-phase)', fontsize=12)
    ax.set_ylabel('虚部 (Quadrature)', fontsize=12)
    ax.set_title('16-QAM星座图（示例）', fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    
    plt.savefig('../examples/16qam_constellation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ 16-QAM示例已生成")
    
    # BER性能曲线示例
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    snr_db = np.arange(0, 16, 2)
    
    # 理论BER曲线（近似）
    from scipy.special import erfc
    
    # BPSK
    ber_bpsk = 0.5 * erfc(np.sqrt(10**(snr_db / 10)))
    
    # QPSK (与BPSK相同)
    ber_qpsk = 0.5 * erfc(np.sqrt(10**(snr_db / 10)))
    
    # 16-QAM (近似)
    ber_qam16 = 0.75 * erfc(np.sqrt(0.4 * 10**(snr_db / 10)))
    
    ax.semilogy(snr_db, ber_bpsk, 'b-o', linewidth=2, markersize=8, label='BPSK')
    ax.semilogy(snr_db, ber_qpsk, 'r-s', linewidth=2, markersize=8, label='QPSK')
    ax.semilogy(snr_db, ber_qam16, 'g-^', linewidth=2, markersize=8, label='16-QAM')
    
    ax.set_xlabel('SNR (dB)', fontsize=12)
    ax.set_ylabel('Bit Error Rate (BER)', fontsize=12)
    ax.set_title('数字调制方式BER性能对比（理论曲线）', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, which='both', alpha=0.3)
    ax.set_ylim(1e-6, 1)
    
    plt.savefig('../examples/ber_curve_example.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ BER曲线示例已生成")
    
    print("\n所有示例图片已保存到 examples/ 目录")


if __name__ == "__main__":
    create_example_constellations()
