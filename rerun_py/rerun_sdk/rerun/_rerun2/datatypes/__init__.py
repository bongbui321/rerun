# NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.

from __future__ import annotations

from .angle import Angle, AngleArray, AngleArrayLike, AngleLike, AngleType
from .annotation_info import (
    AnnotationInfo,
    AnnotationInfoArray,
    AnnotationInfoArrayLike,
    AnnotationInfoLike,
    AnnotationInfoType,
)
from .class_description import (
    ClassDescription,
    ClassDescriptionArray,
    ClassDescriptionArrayLike,
    ClassDescriptionLike,
    ClassDescriptionType,
)
from .class_description_map_elem import (
    ClassDescriptionMapElem,
    ClassDescriptionMapElemArray,
    ClassDescriptionMapElemArrayLike,
    ClassDescriptionMapElemLike,
    ClassDescriptionMapElemType,
)
from .class_id import ClassId, ClassIdArray, ClassIdArrayLike, ClassIdLike, ClassIdType
from .color import Color, ColorArray, ColorArrayLike, ColorLike, ColorType
from .fuzzy import (
    AffixFuzzer1,
    AffixFuzzer1Array,
    AffixFuzzer1ArrayLike,
    AffixFuzzer1Like,
    AffixFuzzer1Type,
    AffixFuzzer2,
    AffixFuzzer2Array,
    AffixFuzzer2ArrayLike,
    AffixFuzzer2Like,
    AffixFuzzer2Type,
    AffixFuzzer3,
    AffixFuzzer3Array,
    AffixFuzzer3ArrayLike,
    AffixFuzzer3Like,
    AffixFuzzer3Type,
    AffixFuzzer4,
    AffixFuzzer4Array,
    AffixFuzzer4ArrayLike,
    AffixFuzzer4Like,
    AffixFuzzer4Type,
    AffixFuzzer5,
    AffixFuzzer5Array,
    AffixFuzzer5ArrayLike,
    AffixFuzzer5Like,
    AffixFuzzer5Type,
    AffixFuzzer20,
    AffixFuzzer20Array,
    AffixFuzzer20ArrayLike,
    AffixFuzzer20Like,
    AffixFuzzer20Type,
    FlattenedScalar,
    FlattenedScalarArray,
    FlattenedScalarArrayLike,
    FlattenedScalarLike,
    FlattenedScalarType,
)
from .fuzzy_deps import (
    PrimitiveComponent,
    PrimitiveComponentArray,
    PrimitiveComponentArrayLike,
    PrimitiveComponentLike,
    PrimitiveComponentType,
    StringComponent,
    StringComponentArray,
    StringComponentArrayLike,
    StringComponentLike,
    StringComponentType,
)
from .keypoint_id import KeypointId, KeypointIdArray, KeypointIdArrayLike, KeypointIdLike, KeypointIdType
from .keypoint_pair import KeypointPair, KeypointPairArray, KeypointPairArrayLike, KeypointPairLike, KeypointPairType
from .label import Label, LabelArray, LabelArrayLike, LabelLike, LabelType
from .mat3x3 import Mat3x3, Mat3x3Array, Mat3x3ArrayLike, Mat3x3Like, Mat3x3Type
from .mat4x4 import Mat4x4, Mat4x4Array, Mat4x4ArrayLike, Mat4x4Like, Mat4x4Type
from .quaternion import Quaternion, QuaternionArray, QuaternionArrayLike, QuaternionLike, QuaternionType
from .rotation3d import Rotation3D, Rotation3DArray, Rotation3DArrayLike, Rotation3DLike, Rotation3DType
from .rotation_axis_angle import (
    RotationAxisAngle,
    RotationAxisAngleArray,
    RotationAxisAngleArrayLike,
    RotationAxisAngleLike,
    RotationAxisAngleType,
)
from .scale3d import Scale3D, Scale3DArray, Scale3DArrayLike, Scale3DLike, Scale3DType
from .tensor_buffer import TensorBuffer, TensorBufferArray, TensorBufferArrayLike, TensorBufferLike, TensorBufferType
from .tensor_data import TensorData, TensorDataArray, TensorDataArrayLike, TensorDataLike, TensorDataType
from .tensor_dimension import (
    TensorDimension,
    TensorDimensionArray,
    TensorDimensionArrayLike,
    TensorDimensionLike,
    TensorDimensionType,
)
from .tensor_id import TensorId, TensorIdArray, TensorIdArrayLike, TensorIdLike, TensorIdType
from .transform3d import Transform3D, Transform3DArray, Transform3DArrayLike, Transform3DLike, Transform3DType
from .translation_and_mat3x3 import (
    TranslationAndMat3x3,
    TranslationAndMat3x3Array,
    TranslationAndMat3x3ArrayLike,
    TranslationAndMat3x3Like,
    TranslationAndMat3x3Type,
)
from .translation_rotation_scale3d import (
    TranslationRotationScale3D,
    TranslationRotationScale3DArray,
    TranslationRotationScale3DArrayLike,
    TranslationRotationScale3DLike,
    TranslationRotationScale3DType,
)
from .vec2d import Vec2D, Vec2DArray, Vec2DArrayLike, Vec2DLike, Vec2DType
from .vec3d import Vec3D, Vec3DArray, Vec3DArrayLike, Vec3DLike, Vec3DType
from .vec4d import Vec4D, Vec4DArray, Vec4DArrayLike, Vec4DLike, Vec4DType

__all__ = [
    "AffixFuzzer1",
    "AffixFuzzer1Array",
    "AffixFuzzer1ArrayLike",
    "AffixFuzzer1Like",
    "AffixFuzzer1Type",
    "AffixFuzzer2",
    "AffixFuzzer20",
    "AffixFuzzer20Array",
    "AffixFuzzer20ArrayLike",
    "AffixFuzzer20Like",
    "AffixFuzzer20Type",
    "AffixFuzzer2Array",
    "AffixFuzzer2ArrayLike",
    "AffixFuzzer2Like",
    "AffixFuzzer2Type",
    "AffixFuzzer3",
    "AffixFuzzer3Array",
    "AffixFuzzer3ArrayLike",
    "AffixFuzzer3Like",
    "AffixFuzzer3Type",
    "AffixFuzzer4",
    "AffixFuzzer4Array",
    "AffixFuzzer4ArrayLike",
    "AffixFuzzer4Like",
    "AffixFuzzer4Type",
    "AffixFuzzer5",
    "AffixFuzzer5Array",
    "AffixFuzzer5ArrayLike",
    "AffixFuzzer5Like",
    "AffixFuzzer5Type",
    "Angle",
    "AngleArray",
    "AngleArrayLike",
    "AngleLike",
    "AngleType",
    "AnnotationInfo",
    "AnnotationInfoArray",
    "AnnotationInfoArrayLike",
    "AnnotationInfoLike",
    "AnnotationInfoType",
    "ClassDescription",
    "ClassDescriptionArray",
    "ClassDescriptionArrayLike",
    "ClassDescriptionLike",
    "ClassDescriptionMapElem",
    "ClassDescriptionMapElemArray",
    "ClassDescriptionMapElemArrayLike",
    "ClassDescriptionMapElemLike",
    "ClassDescriptionMapElemType",
    "ClassDescriptionType",
    "ClassId",
    "ClassIdArray",
    "ClassIdArrayLike",
    "ClassIdLike",
    "ClassIdType",
    "Color",
    "ColorArray",
    "ColorArrayLike",
    "ColorLike",
    "ColorType",
    "FlattenedScalar",
    "FlattenedScalarArray",
    "FlattenedScalarArrayLike",
    "FlattenedScalarLike",
    "FlattenedScalarType",
    "KeypointId",
    "KeypointIdArray",
    "KeypointIdArrayLike",
    "KeypointIdLike",
    "KeypointIdType",
    "KeypointPair",
    "KeypointPairArray",
    "KeypointPairArrayLike",
    "KeypointPairLike",
    "KeypointPairType",
    "Label",
    "LabelArray",
    "LabelArrayLike",
    "LabelLike",
    "LabelType",
    "Mat3x3",
    "Mat3x3Array",
    "Mat3x3ArrayLike",
    "Mat3x3Like",
    "Mat3x3Type",
    "Mat4x4",
    "Mat4x4Array",
    "Mat4x4ArrayLike",
    "Mat4x4Like",
    "Mat4x4Type",
    "PrimitiveComponent",
    "PrimitiveComponentArray",
    "PrimitiveComponentArrayLike",
    "PrimitiveComponentLike",
    "PrimitiveComponentType",
    "Quaternion",
    "QuaternionArray",
    "QuaternionArrayLike",
    "QuaternionLike",
    "QuaternionType",
    "Rotation3D",
    "Rotation3DArray",
    "Rotation3DArrayLike",
    "Rotation3DLike",
    "Rotation3DType",
    "RotationAxisAngle",
    "RotationAxisAngleArray",
    "RotationAxisAngleArrayLike",
    "RotationAxisAngleLike",
    "RotationAxisAngleType",
    "Scale3D",
    "Scale3DArray",
    "Scale3DArrayLike",
    "Scale3DLike",
    "Scale3DType",
    "StringComponent",
    "StringComponentArray",
    "StringComponentArrayLike",
    "StringComponentLike",
    "StringComponentType",
    "TensorBuffer",
    "TensorBufferArray",
    "TensorBufferArrayLike",
    "TensorBufferLike",
    "TensorBufferType",
    "TensorData",
    "TensorDataArray",
    "TensorDataArrayLike",
    "TensorDataLike",
    "TensorDataType",
    "TensorDimension",
    "TensorDimensionArray",
    "TensorDimensionArrayLike",
    "TensorDimensionLike",
    "TensorDimensionType",
    "TensorId",
    "TensorIdArray",
    "TensorIdArrayLike",
    "TensorIdLike",
    "TensorIdType",
    "Transform3D",
    "Transform3DArray",
    "Transform3DArrayLike",
    "Transform3DLike",
    "Transform3DType",
    "TranslationAndMat3x3",
    "TranslationAndMat3x3Array",
    "TranslationAndMat3x3ArrayLike",
    "TranslationAndMat3x3Like",
    "TranslationAndMat3x3Type",
    "TranslationRotationScale3D",
    "TranslationRotationScale3DArray",
    "TranslationRotationScale3DArrayLike",
    "TranslationRotationScale3DLike",
    "TranslationRotationScale3DType",
    "Vec2D",
    "Vec2DArray",
    "Vec2DArrayLike",
    "Vec2DLike",
    "Vec2DType",
    "Vec3D",
    "Vec3DArray",
    "Vec3DArrayLike",
    "Vec3DLike",
    "Vec3DType",
    "Vec4D",
    "Vec4DArray",
    "Vec4DArrayLike",
    "Vec4DLike",
    "Vec4DType",
]
