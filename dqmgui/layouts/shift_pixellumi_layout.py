def shiftpixellumilayout(i, p, *rows): i["00 Shift/PixelLumi/" + p] = DQMItem(layout=rows)

shiftpixellumilayout(dqmitems, "00 - HFDeliveredToPXByLS",
                     [{ 'path': "PixelLumi/PixelLumiDqmZeroBias/HFDeliveredToPXByLS",
                        'description':""}]
                     )

shiftpixellumilayout(dqmitems, "01 - HFRecordedToPXByLS",
                     [{ 'path': "PixelLumi/PixelLumiDqmZeroBias/HFRecordedToPXByLS",
                        'description':""}]
                     )

shiftpixellumilayout(dqmitems, "02 - totalPixelLumiByLS",
                     [{ 'path': "PixelLumi/PixelLumiDqmZeroBias/totalPixelLumiByLS",
                        'description':""}]
                     )

shiftpixellumilayout(dqmitems, "03 - PXLumiByBXsum",
                     [{ 'path': "PixelLumi/PixelLumiDqmZeroBias/PXLumiByBXsum",
                        'description':""}]
                     )

shiftpixellumilayout(dqmitems, "04 - totalHFDeliveredLumiByLS",
                     [{ 'path': "PixelLumi/HF/totalHFDeliveredLumiByLS",
                        'description':""}]
                     )

shiftpixellumilayout(dqmitems, "05 - totalHFRecordedLumiByLS",
                     [{ 'path': "PixelLumi/HF/totalHFRecordedLumiByLS",
                        'description':""}]
                     )

shiftpixellumilayout(dqmitems, "06 - HFRecordedToDeliveredRatioByLS",
                     [{ 'path': "PixelLumi/HF/HFRecordedToDeliveredRatioByLS",
                        'description':""}]
                     )
