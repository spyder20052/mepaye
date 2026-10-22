import Foundation
import Vision
import CoreImage
import ImageIO
import UniformTypeIdentifiers

let args = CommandLine.arguments
let src = URL(fileURLWithPath: args[1]), dst = URL(fileURLWithPath: args[2])
guard let isrc = CGImageSourceCreateWithURL(src as CFURL, nil), let cg = CGImageSourceCreateImageAtIndex(isrc, 0, nil) else { fatalError("lecture") }
let req = VNGenerateForegroundInstanceMaskRequest()
let h = VNImageRequestHandler(cgImage: cg)
try h.perform([req])
guard let obs = req.results?.first else { fatalError("aucun sujet") }
let buf = try obs.generateMaskedImage(ofInstances: obs.allInstances, from: h, croppedToInstancesExtent: false)
let ci = CIImage(cvPixelBuffer: buf)
let ctx = CIContext()
guard let out = ctx.createCGImage(ci, from: ci.extent) else { fatalError("rendu") }
let d = CGImageDestinationCreateWithURL(dst as CFURL, UTType.png.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(d, out, nil)
CGImageDestinationFinalize(d)
print("ok", out.width, out.height)
