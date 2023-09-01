// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.
// Based on "crates/re_types/definitions/rerun/datatypes/tensor_id.fbs"

#pragma once

#include "../result.hpp"

#include <cstdint>
#include <memory>

namespace arrow {
    class DataType;
    class FixedSizeListBuilder;
    class MemoryPool;
} // namespace arrow

namespace rerun {
    namespace datatypes {
        struct TensorId {
            uint8_t uuid[16];

          public:
            TensorId() = default;

            TensorId(const uint8_t (&_uuid)[16])
                : uuid{
                      _uuid[0],
                      _uuid[1],
                      _uuid[2],
                      _uuid[3],
                      _uuid[4],
                      _uuid[5],
                      _uuid[6],
                      _uuid[7],
                      _uuid[8],
                      _uuid[9],
                      _uuid[10],
                      _uuid[11],
                      _uuid[12],
                      _uuid[13],
                      _uuid[14],
                      _uuid[15]} {}

            /// Returns the arrow data type this type corresponds to.
            static const std::shared_ptr<arrow::DataType>& arrow_datatype();

            /// Creates a new array builder with an array of this type.
            static Result<std::shared_ptr<arrow::FixedSizeListBuilder>> new_arrow_array_builder(
                arrow::MemoryPool* memory_pool
            );

            /// Fills an arrow array builder with an array of this type.
            static Error fill_arrow_array_builder(
                arrow::FixedSizeListBuilder* builder, const TensorId* elements, size_t num_elements
            );
        };
    } // namespace datatypes
} // namespace rerun
