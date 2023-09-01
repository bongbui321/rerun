// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.
// Based on "crates/re_types/definitions/rerun/archetypes/tensor.fbs"

#pragma once

#include "../arrow.hpp"
#include "../components/tensor_data.hpp"
#include "../data_cell.hpp"
#include "../result.hpp"

#include <cstdint>
#include <utility>
#include <vector>

namespace rerun {
    namespace archetypes {
        /// A generic n-dimensional Tensor.
        struct Tensor {
            /// The tensor data
            rerun::components::TensorData data;

          public:
            Tensor() = default;

            Tensor(rerun::components::TensorData _data) : data(std::move(_data)) {}

            /// Returns the number of primary instances of this archetype.
            size_t num_instances() const {
                return 1;
            }

            /// Creates a list of Rerun DataCell from this archetype.
            Result<std::vector<rerun::DataCell>> to_data_cells() const;
        };
    } // namespace archetypes
} // namespace rerun
