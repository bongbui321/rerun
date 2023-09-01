// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.

#![allow(trivial_numeric_casts)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]
#![allow(clippy::iter_on_single_items)]
#![allow(clippy::map_flatten)]
#![allow(clippy::match_wildcard_for_single_variants)]
#![allow(clippy::needless_question_mark)]
#![allow(clippy::redundant_closure)]
#![allow(clippy::too_many_arguments)]
#![allow(clippy::too_many_lines)]
#![allow(clippy::unnecessary_cast)]

/// A monochrome or color image.
///
/// The shape of the `TensorData` must be mappable to:
/// - A `HxW` tensor, treated as a grayscale image.
/// - A `HxWx3` tensor, treated as an RGB image.
/// - A `HxWx4` tensor, treated as an RGBA image.
///
/// The viewer has limited support for ignoring extra empty dimensions.
///
/// ## Example
///
/// ```ignore
/// //! Create and log an image
/// use ndarray::{s, Array, ShapeBuilder};
/// use rerun::archetypes::Image;
/// use rerun::{MsgSender, RecordingStreamBuilder};
///
/// fn main() -> Result<(), Box<dyn std::error::Error>> {
///    let (rec_stream, storage) = RecordingStreamBuilder::new(env!("CARGO_BIN_NAME")).memory()?;
///
///    let mut image = Array::<u8, _>::zeros((200, 300, 3).f());
///    image.slice_mut(s![.., .., 0]).fill(255);
///    image.slice_mut(s![50..150, 50..150, 0]).fill(0);
///    image.slice_mut(s![50..150, 50..150, 1]).fill(255);
///
///    let image = Image::try_from(image)?;
///
///    MsgSender::from_archetype("image", &image)?.send(&rec_stream)?;
///
///    rerun::native_viewer::show(storage.take())?;
///    Ok(())
/// }
/// ```
#[derive(Clone, Debug, PartialEq)]
pub struct Image {
    /// The image data. Should always be a rank-2 or rank-3 tensor.
    pub data: crate::components::TensorData,
}

static REQUIRED_COMPONENTS: once_cell::sync::Lazy<[crate::ComponentName; 1usize]> =
    once_cell::sync::Lazy::new(|| ["rerun.components.TensorData".into()]);

static RECOMMENDED_COMPONENTS: once_cell::sync::Lazy<[crate::ComponentName; 0usize]> =
    once_cell::sync::Lazy::new(|| []);

static OPTIONAL_COMPONENTS: once_cell::sync::Lazy<[crate::ComponentName; 0usize]> =
    once_cell::sync::Lazy::new(|| []);

static ALL_COMPONENTS: once_cell::sync::Lazy<[crate::ComponentName; 1usize]> =
    once_cell::sync::Lazy::new(|| ["rerun.components.TensorData".into()]);

impl Image {
    pub const NUM_COMPONENTS: usize = 1usize;
}

impl crate::Archetype for Image {
    #[inline]
    fn name() -> crate::ArchetypeName {
        crate::ArchetypeName::Borrowed("rerun.archetypes.Image")
    }

    #[inline]
    fn required_components() -> &'static [crate::ComponentName] {
        REQUIRED_COMPONENTS.as_slice()
    }

    #[inline]
    fn recommended_components() -> &'static [crate::ComponentName] {
        RECOMMENDED_COMPONENTS.as_slice()
    }

    #[inline]
    fn optional_components() -> &'static [crate::ComponentName] {
        OPTIONAL_COMPONENTS.as_slice()
    }

    #[inline]
    fn all_components() -> &'static [crate::ComponentName] {
        ALL_COMPONENTS.as_slice()
    }

    #[inline]
    fn indicator_component() -> crate::ComponentName {
        "rerun.components.ImageIndicator".into()
    }

    #[inline]
    fn num_instances(&self) -> usize {
        1
    }

    #[inline]
    fn try_to_arrow(
        &self,
    ) -> crate::SerializationResult<
        Vec<(::arrow2::datatypes::Field, Box<dyn ::arrow2::array::Array>)>,
    > {
        use crate::{Loggable as _, ResultExt as _};
        Ok([
            {
                Some({
                    let array = <crate::components::TensorData>::try_to_arrow([&self.data], None);
                    array.map(|array| {
                        let datatype = ::arrow2::datatypes::DataType::Extension(
                            "rerun.components.TensorData".into(),
                            Box::new(array.data_type().clone()),
                            Some("rerun.components.TensorData".into()),
                        );
                        (
                            ::arrow2::datatypes::Field::new("data", datatype, false),
                            array,
                        )
                    })
                })
                .transpose()
                .with_context("rerun.archetypes.Image#data")?
            },
            {
                let datatype = ::arrow2::datatypes::DataType::Extension(
                    "rerun.components.ImageIndicator".to_owned(),
                    Box::new(::arrow2::datatypes::DataType::Null),
                    Some("rerun.components.ImageIndicator".to_owned()),
                );
                let array = ::arrow2::array::NullArray::new(
                    datatype.to_logical_type().clone(),
                    self.num_instances(),
                )
                .boxed();
                Some((
                    ::arrow2::datatypes::Field::new(
                        "rerun.components.ImageIndicator",
                        datatype,
                        false,
                    ),
                    array,
                ))
            },
        ]
        .into_iter()
        .flatten()
        .collect())
    }

    #[inline]
    fn try_from_arrow(
        arrow_data: impl IntoIterator<
            Item = (::arrow2::datatypes::Field, Box<dyn ::arrow2::array::Array>),
        >,
    ) -> crate::DeserializationResult<Self> {
        use crate::{Loggable as _, ResultExt as _};
        let arrays_by_name: ::std::collections::HashMap<_, _> = arrow_data
            .into_iter()
            .map(|(field, array)| (field.name, array))
            .collect();
        let data = {
            let array = arrays_by_name
                .get("data")
                .ok_or_else(crate::DeserializationError::missing_data)
                .with_context("rerun.archetypes.Image#data")?;
            <crate::components::TensorData>::try_from_arrow_opt(&**array)
                .with_context("rerun.archetypes.Image#data")?
                .into_iter()
                .next()
                .flatten()
                .ok_or_else(crate::DeserializationError::missing_data)
                .with_context("rerun.archetypes.Image#data")?
        };
        Ok(Self { data })
    }
}

impl Image {
    pub fn new(data: impl Into<crate::components::TensorData>) -> Self {
        Self { data: data.into() }
    }
}
