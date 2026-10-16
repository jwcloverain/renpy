"""Regression checks for the native FFmpeg media reader."""

from pathlib import Path


def test_read_packet_releases_packet_on_eof():
    source = (Path(__file__).parents[1] / "module" / "ffmedia.c").read_text(encoding="utf-8")
    read_frame = source.index("if (av_read_frame(ms->ctx, pkt))")
    end = source.index("\n\t\t}", read_frame)
    block = source[read_frame:end]

    assert "av_packet_free(&pkt);" in block

