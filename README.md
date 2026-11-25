# pairwise-gradient-deband-mask

## 领域

游戏、图形与多媒体

## 主题

梯度去色带自适应抖动

## 说明

多通道阶梯检测、内容自适应幅度、逐帧种子。

初始状态下 `imaging/gradient_deband.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
